from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location( models.Model ):
    name=models.CharField( max_length=30 )

    def save_location(self):
        self.save( )

    def delete_location(self):
        self.delete( )

    def __str__(self):
        return self.name


class Image( models.Model ):
    image=models.ImageField( upload_to='images/' , )
    name=models.CharField( max_length=40 )
    user=models.ForeignKey( User , on_delete=models.CASCADE , blank=True , related_name="images" )
    description=models.TextField( )
    location=models.ForeignKey( Location , null=True )
    likes=models.IntegerField( default=0 )
    comments=models.TextField( blank=True )

    def __str__(self):
        return self.name

    def save_image(self):
        self.save( )

    @classmethod
    def delete_image_by_id(cls , id):
        pictures=cls.objects.filter( pk=id )
        pictures.delete( )

    @classmethod
    def get_image_by_id(cls , id):
        pictures=cls.objects.get( pk=id )
        return pictures

    @classmethod
    def filter_by_tag(cls , tags):
        pictures=cls.objects.filter( tags=tags )
        return pictures

    @classmethod
    def filter_by_location(cls , location):
        pictures=cls.objects.filter( location=location )
        return pictures

    @classmethod
    def search_image(cls , search_term):
        pictures=cls.objects.filter( name__icontains=search_term )
        return pictures

    @classmethod
    def update_image(cls , id):
        pictures=cls.objects.filter( id=id ).update( id=id )
        return pictures

    @classmethod
    def update_description(cls , id):
        pictures=cls.objects.filter( id=id ).update( id=id )
        return pictures


class Neighbourhood( models.Model ):
    CITY_CHOICES=(
        ('Nairobi' , 'Nairobi') ,
        ('Machakos' , 'Machakos') ,
        ('KItui' , 'KItui') ,
        ('Garissa' , 'Garissa') ,
        ('Mombasa' , 'Mombasa') ,
        ('Malindi' , 'Malindi') ,
        ('Kisumu' , 'Kisumu') ,
        ('Migori' , 'Migori') ,
        ('Kakamega' , 'Kakamega') ,
        ('Uasingishu' , 'Uasingishu') ,

    )

    neighbourhood_name=models.CharField( max_length=30 )
    neighbourhood_location=models.CharField( choices=CITY_CHOICES , max_length=200 , default=0 , null=True ,
                                             blank=True )
    population=models.IntegerField( default=0 , null=True , blank=True )

    def __str__(self):
        return self.neighbourhood_name

    def save_neighbourhood(self):
        self.save( )

    @classmethod
    def delete_neighbourhood_by_id(cls , id):
        neighbourhoods=cls.objects.filter( pk=id )
        neighbourhoods.delete( )

    @classmethod
    def get_neighbourhood_by_id(cls , id):
        neighbourhoods=cls.objects.get( pk=id )
        return neighbourhoods

    @classmethod
    def filter_by_location(cls , location):
        neighbourhoods=cls.objects.filter( location=location )
        return neighbourhoods

    @classmethod
    def search_neighbourhood(cls , search_term):
        neighbourhoods=cls.objects.filter( neighbourhood_name__icontains=search_term )
        return neighbourhoods

    @classmethod
    def update_neighbourhood(cls , id):
        neighbourhoods=cls.objects.filter( id=id ).update( id=id )
        return neighbourhoods

    @classmethod
    def update_neighbourhood(cls , id):
        neighbourhoods=cls.objects.filter( id=id ).update( id=id )
        return neighbourhoods


class Business( models.Model ):
    business_name=models.CharField( max_length=30 , null=True )
    user=models.ForeignKey( User , on_delete=models.CASCADE , null=True , related_name="business" )
    neighbourhood=models.ForeignKey( Neighbourhood , on_delete=models.CASCADE ,
                                        related_name="neighbourhoodbusiness" , null=True , blank=True )
    email_address=models.CharField( max_length=200 , null=True )

    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save( )

    @classmethod
    def delete_business_by_id(cls , id):
        businesses=cls.objects.filter( pk=id )
        businesses.delete( )

    @classmethod
    def get_businesses_by_id(cls , id):
        businesses=cls.objects.get( pk=id )
        return businesses

    @classmethod
    def filter_by_location(cls , location):
        businesses=cls.objects.filter( location=location )
        return businesses

    @classmethod
    def search_businesses(cls , search_term):
        businesses=cls.objects.filter( business_name__icontains=search_term )
        return businesses

    @classmethod
    def update_business(cls , id):
        businesses=cls.objects.filter( id=id ).update( id=id )
        return businesses

    @classmethod
    def update_business(cls , id):
        businesses=cls.objects.filter( id=id ).update( id=id )
        return businesses



    def save_project(self):
        self.save( )

    @classmethod
    def delete_project_by_id(cls , id):
        projects=cls.objects.filter( pk=id )
        projects.delete( )

    @classmethod
    def get_project_by_id(cls , id):
        projects=cls.objects.get( pk=id )
        return projects

    @classmethod
    def search_projects(cls , search_term):
        projects=cls.objects.filter( title__icontains=search_term )
        return projects

    @classmethod
    def update_project(cls , id):
        projects=cls.objects.filter( id=id ).update( id=id )
        return projects

    @classmethod
    def update_description(cls , id):
        projects=cls.objects.filter( id=id ).update( id=id )
        return projects

    def __str__(self):
        return self.title


class Profile( models.Model ):
    bio=models.TextField( max_length=200 , null=True , blank=True , default="bio" )
    profile_pic=models.ImageField( upload_to='picture/' , null=True , blank=True , default=0 )
    user=models.OneToOneField( User , on_delete=models.CASCADE , null=True , related_name="profile" )
    project=models.ForeignKey( Project , null=True )
    email=models.TextField( max_length=200 , null=True , blank=True , default=0 )
    neighbourhood_id=models.ForeignKey( Neighbourhood , on_delete=models.CASCADE , related_name="neighbourhood" ,
                                        null=True , blank=True )

    def create_user_profile(sender , instance , created , **kwargs):
        if created:
            Profile.objects.create( user=instance )

    def save_profile(self):
        self.save( )

    def delete_profile(self):
        self.delete( )

    @classmethod
    def search_users(cls , search_term):
        profiles=cls.objects.filter( user__username__icontains=search_term )
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr( self.profile_pic , 'url' ):
            return self.profile_pic.url

    def __str__(self):
        return self.user.username


class Review( models.Model ):
    RATING_CHOICES=(
        (1 , '1') ,
        (2 , '2') ,
        (3 , '3') ,
        (4 , '4') ,
        (5 , '5') ,
        (6 , '6') ,
        (7 , '7') ,
        (8 , '8') ,
        (9 , '9') ,
        (10 , '10') ,

    )
    project=models.ForeignKey( Project , null=True , blank=True , on_delete=models.CASCADE , related_name="reviews" )
    user=models.ForeignKey( User , null=True , blank=True , on_delete=models.CASCADE , related_name='reviews' )
    image=models.ForeignKey( Image , on_delete=models.CASCADE , related_name="reviews" , null=True , blank=True )
    comment=models.TextField( )
    design_rating=models.IntegerField( choices=RATING_CHOICES , default=0 )
    usability_rating=models.IntegerField( choices=RATING_CHOICES , default=0 )
    content_rating=models.IntegerField( choices=RATING_CHOICES , default=0 )

    def save_comment(self):
        self.save( )

    def get_comment(self , id):
        comments=Review.objects.filter( image_id=id )
        return comments

    def __str__(self):
        return self.comment


class NewsLetterRecipients( models.Model ):
    name=models.CharField( max_length=30 )
    email=models.EmailField( )


class Comments( models.Model ):
    '''
	Model will handle comments made to a post resource
	'''
    comment=models.CharField( max_length=600 )
    user=models.ForeignKey( User )
    project=models.ForeignKey( Project )

    def save_comment(self):
        self.save( )

    def delete_comment(self):
        self.delete( )

    def __str__(self):
        return self.comment

class Project( models.Model ):
    title=models.TextField( max_length=200 , null=True , blank=True , default="title" )
    project_image=models.ImageField( upload_to='project/' , null=True , blank=True )
    description=models.TextField( )
    user=models.ForeignKey( User , on_delete=models.CASCADE , related_name="neighbourhoodproject" , null=True ,
                            blank=True )
    neighbourhood=models.ForeignKey( Neighbourhood , on_delete=models.CASCADE , related_name="neighbourhoodproject" ,
                                     null=True , blank=True )
    postDate=models.DateTimeField( auto_now_add=True )
    location=models.ForeignKey( Location , on_delete=models.CASCADE,null=True )
    comment=models.ForeignKey( Comments ,on_delete=models.CASCADE, null=True )
    profile=models.ForeignKey( Profile , on_delete=models.CASCADE,null=True )
    review=models.ForeignKey( Review , on_delete=models.CASCADE,null=True )



