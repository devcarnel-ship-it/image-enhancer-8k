# 🖼️ Image Enhancer 8K

سكريبت احترافي لتحسين جودة الصور وتحويلها إلى دقة **8K (7680x4320)**

## ✨ المميزات

- ✅ تحويل الصور إلى **8K** بدقة عالية
- ✅ إزالة الضوضاء باستخدام **Non-Local Means Denoising**
- ✅ تحسين التباين والحدة تلقائياً
- ✅ دعم عدة طرق للحقن (Lanczos4, Cubic, Linear)
- ✅ واجهة سطر أوامر احترافية
- ✅ معالجة سريعة وفعالة

## 📋 المتطلبات

- Python 3.7+
- OpenCV
- NumPy

## 🚀 التثبيت

### 1. استنساخ المستودع
```bash
git clone https://github.com/devcarnel-ship-it/image-enhancer-8k.git
cd image-enhancer-8k
```

### 2. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

## 💻 طريقة الاستخدام

### الاستخدام الأساسي
```bash
python image_enhancer_8k.py your_image.jpg
```

### تحديد صورة الخرج
```bash
python image_enhancer_8k.py input.jpg -o output_8k.jpg
```

### تخطي خطوات معينة
```bash
# تخطي إزالة الضوضاء
python image_enhancer_8k.py input.jpg --no-denoise

# تخطي الشحذ
python image_enhancer_8k.py input.jpg --no-sharpen

# تخطي كلاهما
python image_enhancer_8k.py input.jpg --no-denoise --no-sharpen
```

### تحديد طريقة الحقن
```bash
python image_enhancer_8k.py input.jpg -m cubic
```
الخيارات: `lanczos4` (الافتراضي), `cubic`, `linear`

### تحديد جودة الصورة المخرجة
```bash
python image_enhancer_8k.py input.jpg -q 90
```
القيمة من 1 إلى 100 (الافتراضي: 95)

## 📊 أمثلة متقدمة

```bash
# تحسين كامل مع جودة عالية
python image_enhancer_8k.py photo.jpg -o enhanced_8k.jpg -q 98

# تحسين بدون إزالة ضوضاء باستخدام Cubic interpolation
python image_enhancer_8k.py photo.jpg --no-denoise -m cubic

# مساعدة وخيارات إضافية
python image_enhancer_8k.py --help
```

## 🔧 الخيارات الكاملة

```
الاستخدام: python image_enhancer_8k.py [-h] [-o OUTPUT] [-m {lanczos4,cubic,linear}]
                                         [--no-denoise] [--no-sharpen] [-q QUALITY]
                                         input_image

المعاملات المطلوبة:
  input_image              مسار الصورة المدخلة

المعاملات الاختيارية:
  -h, --help              عرض رسالة المساعدة
  -o, --output OUTPUT     مسار الصورة المخرجة (الافتراضي: output_8k.jpg)
  -m, --method            طريقة الحقن (الافتراضي: lanczos4)
  --no-denoise            تخطي إزالة الضوضاء
  --no-sharpen            تخطي الشحذ
  -q, --quality QUALITY   جودة الصورة من 1 إلى 100 (الافتراضي: 95)
```

## 📈 مراحل المعالجة

1. **إزالة الضوضاء** - تنظيف الصورة من الضوضاء
2. **تحسين التباين** - تحسين الحدود والتفاصيل
3. **الشحذ** - تحديد الحواف والتفاصيل الدقيقة
4. **الحقن إلى 8K** - تكبير الصورة إلى 7680x4320

## 📝 ملاحظات مهمة

- الصور الكبيرة قد تحتاج وقتاً أطول للمعالجة
- تأكد من وجود مساحة تخزين كافية (الصور 8K كبيرة الحجم)
- جودة النتيجة تعتمد على جودة الصورة الأصلية
- استخدم `lanczos4` للحصول على أفضل النتائج

## 🐛 استكشاف الأخطاء

### خطأ: لم يتم العثور على الصورة
```bash
# تأكد من أن مسار الصورة صحيح
python image_enhancer_8k.py /path/to/image.jpg
```

### الصورة بطيئة جداً
```bash
# استخدم linear بدلاً من lanczos4
python image_enhancer_8k.py input.jpg -m linear
```

### خطأ في الذاكرة
```bash
# تأكد من توفر ذاكرة كافية (تحتاج صور 8K إلى ~150MB+)
```

## 📄 الترخيص

هذا المشروع مفتوح المصدر ومتاح للاستخدام الحر

## 👨‍💻 المساهمة

نرحب بمساهماتك! يرجى فتح Issue أو Pull Request

## 📧 التواصل

للأسئلة والاقتراحات: [devcarnel-ship-it](https://github.com/devcarnel-ship-it)

---

**استمتع بتحسين صورك إلى 8K! 🚀**