from django import http
from catalog import models, forms
import jinja2

env = jinja2.Environment(extensions=['jinja2.ext.loopcontrols'],
        loader=jinja2.PackageLoader('hosting-choice', 'templates'))

def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

env.filters['datetimeformat'] = datetimeformat
env.filters['smart_round'] = lambda num: round(num / 0.5) * 0.5


def render_to_response(template, context = None):
    global env

    if context is None:
        context = {}

    obj = env.get_template(template)
    contents = obj.render(**context)

    return http.HttpResponse(contents)


def render(template, context):
    """Generic render method to render full pages"""

    categories = models.Category.objects.filter()

    context.update({
        'categories': categories})

    return render_to_response(template, context)


def show_host(request, slug):
    """Return the view for an host listing"""

    messages = {'success': [], 'errors': []}
    try:
        host = models.Host.objects.get(slug=slug)

        if request.method == 'POST':
            form = forms.CommentForm(request.POST)
            if form.is_valid():

                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                website = form.cleaned_data.get('website', None)
                text = form.cleaned_data['text']

                comment = models.Comment(host=host, name=name,
                    email=email, website=website, text=text, active=True)

                comment.save()

                for name in ['Features', 'Uptime', 'Support']:
                    value = form.cleaned_data.get('rating_'+name.lower()+'_val', -1)
                    type = models.RatingType.objects.get(name=name)
                    rating = models.Rating(type=type, value=value,
                        comment=comment)
                    rating.save()

                messages['success'].append(
                    'Successfully added your review to the site')




        else:
            form = forms.CommentForm()

    except models.Host.DoesNotExist:
        host = None
        form = None

    return render('host.html', {
        'host': host,
        'form': form,
        'messages': messages})

    
def show_category(request, slug):
    """Return the view for a category listing"""

    try:
        category = models.Category.objects.get(slug=slug)
        hosts = models.Host.objects.filter(category=category)
    except models.Category.DoesNotExist:
        category = None
        hosts = []

    return render('category.html', {
        'hosts': hosts,
        'category': category})
