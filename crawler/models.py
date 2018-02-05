from django.db import models

class Crawl(models.Model): 
    project    = models.ForeignKey('Project', on_delete = models.CASCADE)
    nb_url     = models.IntegerField()
    depth      = models.IntegerField(blank=True, null = True)
    date_crawl = models.DateField()


class Project(models.Model): 
    name       = models.CharField(max_length=50)
    user       = models.ForeignKey('user.User', on_delete = models.CASCADE)
    created_at = models.DateField()
    domain     = models.CharField(max_length=200)


class Link(models.Model): 
    follow   = models.BooleanField(default = True) 
    internal = models.BooleanField()
    url      = models.ForeignKey('UrlDetail', on_delete = models.CASCADE)
    anchor   = models.CharField(max_length=200, blank = True)


class UrlDetail(models.Model): 
    url            = models.CharField(max_length=500)
    title          = models.CharField(max_length=500, blank=True, null=True)
    meta_desc      = models.CharField(max_length=500, blank=True, null=True)
    meta_kw        = models.CharField(max_length=200, blank=True, null=True)
    canonical      = models.CharField(max_length=500, blank=True, null=True)
    response_code  = models.IntegerField()
    response_time  = models.FloatField()
    noindex_robot  = models.BooleanField()
    nofollow_robot = models.BooleanField()
    in_sitemap     = models.BooleanField()
    nb_words       = models.IntegerField()
    html_content   = models.TextField()
    first_h1       = models.CharField(max_length=200, blank=True, null=True)
    crawl          = models.ForeignKey('Crawl', on_delete = models.CASCADE)
     

class GlobalStat(models.Model): 
    crawl            = models.ForeignKey('Crawl', on_delete = models.CASCADE)
    nb_200           = models.IntegerField(blank=True, null=True)
    nb_301           = models.IntegerField(blank=True, null=True)
    nb_302           = models.IntegerField(blank=True, null=True)
    nb_404           = models.IntegerField(blank=True, null=True)
    nb_500           = models.IntegerField(blank=True, null=True)
    outlinks_avg     = models.FloatField(blank=True, null=True)
    inlinks_avg      = models.FloatField(blank=True, null=True)
    avg_words        = models.FloatField(blank=True, null=True)
    nb_follow        = models.IntegerField(blank=True, null=True)
    nb_nofollow      = models.IntegerField(blank=True, null=True)
    low_content      = models.IntegerField(blank=True, null=True)
    missing_title    = models.IntegerField(blank=True, null=True)
    too_short_title  = models.IntegerField(blank=True, null=True)
    too_long_title   = models.IntegerField(blank=True, null=True)
    perfect_title    = models.IntegerField(blank=True, null=True)
    missing_desc     = models.IntegerField(blank=True, null=True)
    too_short_desc   = models.IntegerField(blank=True, null=True)
    perfect_desc     = models.IntegerField(blank=True, null=True)
    too_long_desc    = models.IntegerField(blank=True, null=True)
    duplicate_title  = models.IntegerField(blank=True, null=True)
    duplicate_desc   = models.IntegerField(blank=True, null=True)
    indexable_url    = models.IntegerField(blank=True, null=True)
    nb_canonical     = models.IntegerField(blank=True, null=True)
    perfect_loadtime = models.IntegerField(blank=True, null=True)
    medium_loadtime  = models.IntegerField(blank=True, null=True)
    slow_loadtime    = models.IntegerField(blank=True, null=True)
    words_150        = models.IntegerField(blank=True, null=True)
    words_150_300    = models.IntegerField(blank=True, null=True)
    words_300_500    = models.IntegerField(blank=True, null=True)
    words_500_800    = models.IntegerField(blank=True, null=True)
    words_800_1200   = models.IntegerField(blank=True, null=True)
    words_1200       = models.IntegerField(blank=True, null=True)
    


class UrlStat(models.Model): 
    url          = models.ForeignKey('UrlDetail', on_delete = models.CASCADE)
    outlinks     = models.IntegerField(blank=True, null=True)
    inlinks      = models.IntegerField(blank=True, null=True)
    title_length = models.IntegerField(blank=True, null=True)
    desc_length  = models.IntegerField(blank=True, null=True)
    depth_level  = models.IntegerField(blank=True, null=True)
    h1           = models.IntegerField(blank=True, null=True)
    h2           = models.IntegerField(blank=True, null=True)
    h3           = models.IntegerField(blank=True, null=True)
    h4           = models.IntegerField(blank=True, null=True)
    h5           = models.IntegerField(blank=True, null=True)
    h6           = models.IntegerField(blank=True, null=True)
    