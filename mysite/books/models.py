from django.db import models

# Create your models here.

#class BookManager(models.Manager):
#    def title_count(self, keyword):
#        return self.filter(title__icontains=keyword).count()

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['-name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author) #create table books_book_authors
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)
    #objects_filter = BookManager()

    def __unicode__(self):
        return self.title

'''
BEGIN;
CREATE TABLE "books_publisher" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "address" varchar(50) NOT NULL,
    "city" varchar(60) NOT NULL,
    "state_province" varchar(30) NOT NULL,
    "country" varchar(50) NOT NULL,
    "website" varchar(200) NOT NULL
)
;
CREATE TABLE "books_author" (
    "id" integer NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(40) NOT NULL,
    "email" varchar(75) NOT NULL
)
;
CREATE TABLE "books_book_authors" (
    "id" integer NOT NULL PRIMARY KEY,
    "book_id" integer NOT NULL,
    "author_id" integer NOT NULL REFERENCES "books_author" ("id"),
    UNIQUE ("book_id", "author_id")
)
;
CREATE TABLE "books_book" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(100) NOT NULL,
    "publisher_id" integer NOT NULL REFERENCES "books_publisher" ("id"),
    "publication_date" date NOT NULL
)
;
CREATE INDEX "books_book_authors_36c249d7" ON "books_book_authors" ("book_id");
CREATE INDEX "books_book_authors_e969df21" ON "books_book_authors" ("author_id");
CREATE INDEX "books_book_81b79144" ON "books_book" ("publisher_id");

COMMIT;
'''
