"""
Image Quality Enhancement to 8K Resolution
This script upscales images to 8K resolution using various enhancement techniques.
"""

import cv2
import numpy as np
from pathlib import Path
import argparse
from typing import Tuple
import os


class ImageEnhancer8K:
    """
    A class to enhance image quality and upscale to 8K resolution (7680x4320)
    """
    
    # 8K resolution dimensions
    K8_WIDTH = 7680
    K8_HEIGHT = 4320
    
    def __init__(self, upscale_method: str = 'lanczos4'):
        """
        Initialize the image enhancer
        
        Args:
            upscale_method: Interpolation method ('lanczos4', 'cubic', 'linear')
        """
        self.upscale_method = self._get_interpolation_method(upscale_method)
        
    @staticmethod
    def _get_interpolation_method(method: str):
        """Get OpenCV interpolation method"""
        methods = {
            'lanczos4': cv2.INTER_LANCZOS4,
            'cubic': cv2.INTER_CUBIC,
            'linear': cv2.INTER_LINEAR,
            'nearest': cv2.INTER_NEAREST
        }
        return methods.get(method.lower(), cv2.INTER_LANCZOS4)
    
    def enhance_contrast(self, image: np.ndarray, alpha: float = 1.5, 
                        beta: float = 0) -> np.ndarray:
        """Enhance image contrast"""
        enhanced = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        return enhanced
    
    def denoise_image(self, image: np.ndarray, h: int = 10) -> np.ndarray:
        """Denoise image using Non-Local Means Denoising"""
        if len(image.shape) == 3 and image.shape[2] == 3:
            denoised = cv2.fastNlMeansDenoisingColored(image, None, h=h)
        else:
            denoised = cv2.fastNlMeansDenoising(image, None, h=h)
        return denoised
    
    def sharpen_image(self, image: np.ndarray, kernel_strength: float = 1.5) -> np.ndarray:
        """Sharpen image using unsharp mask"""
        blurred = cv2.GaussianBlur(image, (0, 0), 2.0)
        sharpened = cv2.addWeighted(image, 1.0 + kernel_strength, 
                                   blurred, -kernel_strength, 0)
        return np.clip(sharpened, 0, 255).astype(np.uint8)
    
    def upscale_to_8k(self, image: np.ndarray) -> np.ndarray:
        """Upscale image to 8K resolution"""
        upscaled = cv2.resize(image, (self.K8_WIDTH, self.K8_HEIGHT), 
                             interpolation=self.upscale_method)
        return upscaled
    
    def process_image(self, image_path: str, denoise: bool = True, 
                     sharpen: bool = True, enhance_contrast: bool = True) -> np.ndarray:
        """Process and enhance image with all techniques"""
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not read image from {image_path}")
        
        print(f"الحجم الأصلي: {image.shape[1]}x{image.shape[0]}")
        
        if denoise:
            print("جاري إزالة الضوضاء...")
            image = self.denoise_image(image)
        
        if enhance_contrast:
            print("جاري تحسين التباين...")
            image = self.enhance_contrast(image, alpha=1.3, beta=10)
        
        if sharpen:
            print("جاري شحذ الصورة...")
            image = self.sharpen_image(image, kernel_strength=1.2)
        
        print("جاري تحويل إلى 8K...")
        image = self.upscale_to_8k(image)
        
        print(f"الحجم النهائي: {image.shape[1]}x{image.shape[0]} (8K)")
        
        return image
    
    def save_image(self, image: np.ndarray, output_path: str, quality: int = 95) -> None:
        """Save enhanced image"""
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
            cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])
        else:
            cv2.imwrite(output_path, image)
        
        print(f"✓ تم حفظ الصورة في: {output_path}")


def main():
    """Main function with CLI argument parsing"""
    parser = argparse.ArgumentParser(description='تحسين جودة الصور وتحويلها إلى 8K')
    parser.add_argument('input_image', help='مسار الصورة المدخلة')
    parser.add_argument('-o', '--output', default='output_8k.jpg',
                       help='مسار الصورة المخرجة')
    parser.add_argument('-m', '--method', choices=['lanczos4', 'cubic', 'linear'],
                       default='lanczos4', help='طريقة الحقن')
    parser.add_argument('--no-denoise', action='store_true', help='تخطي إزالة الضوضاء')
    parser.add_argument('--no-sharpen', action='store_true', help='تخطي الشحذ')
    parser.add_argument('-q', '--quality', type=int, default=95, help='جودة الصورة (1-100)')
    
    args = parser.parse_args()
    
    if not Path(args.input_image).exists():
        print(f"خطأ: لم يتم العثور على الصورة '{args.input_image}'")
        return
    
    enhancer = ImageEnhancer8K(upscale_method=args.method)
    
    try:
        enhanced_image = enhancer.process_image(
            args.input_image,
            denoise=not args.no_denoise,
            sharpen=not args.no_sharpen
        )
        enhancer.save_image(enhanced_image, args.output, quality=args.quality)
        print("\n✓ تم تحسين الصورة بنجاح!")
    except Exception as e:
        print(f"خطأ: {e}")


if __name__ == '__main__':
    main()