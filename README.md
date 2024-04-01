# ShopAdmin
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Product
Category
Shop
User
kabi endpoind lar ro'yxatini ko'rishingiz mukin

User - bu yerda superuser yordamchi adminlarni qo'shishi o'chirishi va tahrirlashi mumik.
Superuser yordamchi admin maxsulatlar boshqaruvchisi yoki do'konlarboshqaruvchi ekanligini belgilaydi (admin_shop, admin_product)

Shop - Superuser yoki shop_admin Shop obektini yaratish, tahrirlash va o'chirib tashlash imkoniga ega qolganlar uchun faqa ko'rishruxsati bor
do'konlar aro qidiriv do'kon nomi (name) maydoni bo'yicha amalga oshiriladi agar shu nom bilan bir yoki bir nechta do'konlar topilsa ularni ro'yxatini qataradi aks xolda [] ni qaytaradi.

Category - Bu bo'limda kategoriyalar yaratiladi.
Kategoriya yaratish uchun so'rov yuborayotgan user is_staff=True bo'lishi kerak.
kategoriyaga nom, tafsif, kera bolsa qaysi kategoriyaga tegishli (category parent) belgilashi mukmin.

Kategoriyalar bo'ylab qidiruv - qidiruv id, title, paret__id maydonlari bo'ylab olib boriladi va mos category ni qaytaradi agar bunday category topilmasa [] ni qaytaradi.


Produc - Superuser yoki product_admin product obeklarini yaratishi, tahrirlashi va o'chirib tashlashi mumkin. Qolganlar uchun faqat ko'shir imkonyati berilgan.
swaggerning product bo'limidagi get metotida {
search maydiniga maxulot id si yoki maxsulot nomini kiriting orqali qidiruvni amalga oshirish mumkin.
maxulotlarni ro'yxatini olganda maxsulot rasmi sifatida product.main_image metodini to'llash kerak, maxsulotni aosiy rasmi uchun ham.
maxsulotni active xolati bo'yicha filterlash uchun get metotidafi active qismidan kerakli xolatni tanlash mumkin.
maxsulotni narx diapazoni(oralig'i) bo'yicha filterlash uchun prica_max (gacha) price_min (dan) maydonlariga kerakli qiymatlarni kiriting 
}


BU documentation qo'ldan kelganicha yozildi kamchiliklar uchun uzr so'rayman😊😊😊 soat 3:33







