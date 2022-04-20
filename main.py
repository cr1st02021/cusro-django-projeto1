recipes = Recipe.objects.filter(
    category__id=4,
    is_published=True
).order_by('-id')
