# 🏙️ Homashahr Municipality Project

پروژه‌ی **Homashahr Municipality** یک وب‌اپلیکیشن مبتنی بر Django است که برای مدیریت اطلاعات شهرداری، شورا، شهردار، مشاهیر، پروژه‌ها، اخبار و سایر بخش‌های مرتبط طراحی شده است.

---

## 📂 ساختار پوشه‌ها

homashahr/
├── settings.py                    # تنظیمات اصلی پروژه Django
└── urls-project.py            # مسیرهای کلی پروژه

municipality/
├── templates/           # قالب‌های HTML
│   ├── base.html
│   ├── form-celebrities.html
│   ├── form-councils.html
│   ├── form-history.html
│   ├── form-martyrs.html
│   ├── form-mayor.html
│   ├── form-municipality-info.html
│   ├── form-news.html
│   ├── form-personnel.html
│   ├── form-projects.html
│   ├── index.html
│   ├── index2.html
│   ├── list-celebrities.html
│   ├── list-councils.html
│   ├── list-history.html
│   ├── list-martyrs.html
│   ├── list-mayor.html
│   ├── list-municipality-info.html
│   ├── list-news.html
│   ├── list-personnel.html
│   ├── list-projects.html
│   ├── martyr.html
│   ├── shahrdar.html
│   └── shora.html
│
├── admin.py                          # تنظیمات پنل مدیریت Django
├── apps.py                            # پیکربندی اپلیکیشن municipality
├── forms.py                          # فرم‌های Django برای ورود داده‌ها
├── models.py                        # مدل‌های پایگاه داده
├── test.py                            # تست‌های واحد
├── urls.py                            # مسیرهای اپلیکیشن municipality
└── views.py                          # کنترلرها و منطق نمایشی
