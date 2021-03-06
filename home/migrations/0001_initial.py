# Generated by Django 3.1.8 on 2021-04-21 18:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modelcluster.contrib.taggit
import modelcluster.fields
import phonenumber_field.modelfields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailcore', '0061_auto_20210421_2013'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompanyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('about_company_text', wagtail.core.fields.RichTextField(verbose_name='Текст о компании')),
                ('about_company_text_ru', wagtail.core.fields.RichTextField(null=True, verbose_name='Текст о компании')),
                ('about_company_text_uk', wagtail.core.fields.RichTextField(null=True, verbose_name='Текст о компании')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HeadingNewsPublicationsTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name_heading_ru', models.CharField(max_length=255, verbose_name='Название рубрики')),
                ('name_heading_uk', models.CharField(max_length=255, verbose_name='Назва рубрики')),
            ],
            options={
                'verbose_name': 'Рубрики для новостей/публикаций',
                'verbose_name_plural': 'Рубрики для новостей/публикаций',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('contact_data_email', models.EmailField(default='example@mail.com', max_length=254, verbose_name='Email для связи')),
                ('contact_data_phone', phonenumber_field.modelfields.PhoneNumberField(default='+380999999999', max_length=128, region='UA', verbose_name='Контактный номер')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('body_ru', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('body_uk', wagtail.core.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewsPublicationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('publication_title', models.CharField(max_length=255, verbose_name='Название публикации/новости')),
                ('publication_title_ru', models.CharField(max_length=255, null=True, verbose_name='Название публикации/новости')),
                ('publication_title_uk', models.CharField(max_length=255, null=True, verbose_name='Название публикации/новости')),
                ('publication_text', models.TextField(max_length=10000, verbose_name='Текст публикации/новости')),
                ('publication_text_ru', models.TextField(max_length=10000, null=True, verbose_name='Текст публикации/новости')),
                ('publication_text_uk', models.TextField(max_length=10000, null=True, verbose_name='Текст публикации/новости')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации/новости')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания публикации/новости')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения публикации/новости')),
                ('caption', models.CharField(blank=True, max_length=255, verbose_name='Подпись к изображению')),
                ('caption_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Подпись к изображению')),
                ('caption_uk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Подпись к изображению')),
                ('publication_heading', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='home.headingnewspublicationstypes', verbose_name='Название рубрики')),
                ('publication_heading_2', models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, related_name='publication_2', to='home.headingnewspublicationstypes', verbose_name='Название рубрики')),
                ('publication_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='NewsPublicationPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='home.newspublicationpage', verbose_name='Теги')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_newspublicationpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='newspublicationpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='home.NewsPublicationPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='HomeHeaderGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250, verbose_name='Подпись к изображению')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeadingNewsPublications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('heading_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heading_name', to='home.headingnewspublicationstypes', verbose_name='Рубрика')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_page_headings', to='home.newspublicationpage', verbose_name='Страница новости')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('kind_of_activity', models.TextField(max_length=1000, verbose_name='Вид деятельности')),
                ('kind_of_activity_ru', models.TextField(max_length=1000, null=True, verbose_name='Вид деятельности')),
                ('kind_of_activity_uk', models.TextField(max_length=1000, null=True, verbose_name='Вид деятельности')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='home.aboutcompanypage', verbose_name='Вид деятельности')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='aboutcompanypage',
            name='page',
            field=modelcluster.fields.ParentalKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='about_company', to='home.homepage', verbose_name='О компании'),
        ),
    ]
