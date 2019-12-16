from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .data_base_handler import DataBaseTableHandler
from .models import Aliment, UserLinkToAlimentsTable
from .console_display import console_display
from substitute.open_food_facts_handler import OpenFoodFactsAPIHandler


def search_view(request):
    """
    Display a list of similar aliments based on user's query.
    :param request: User's request
    :return:
    """

    # Collect the User's request
    query = request.GET.get('userSearch')
    # Display
    console_display("User's request: " + query)

    # Ensure that the query is filled
    if query:
        # Gather a list from database
        aliment_name = Aliment.objects.filter(name__icontains=query)
        # Check if we find some elements
        if not aliment_name.exists():
            # No result found message
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
            aliment_list = []
        else:
            # Look for similar aliment
            message = "Vous pouvez remplacer cet aliment par:"
            # Collect a list of aliment with the same categories
            aliment_list = Aliment.objects.filter(category__icontains=aliment_name[0].category).order_by('nutriscore')

    else:
        # No query send
        message = "Vous n'avez pas spécifié votre recherche. Voici notre liste."
        aliment_list = Aliment.objects.all()

    # Slice page
    paginator = Paginator(aliment_list, 6)
    # Get the current page
    page = request.GET.get('page')

    # Return only this page substitute and not others
    try:
        aliments = paginator.page(page)
        print("Page OK")
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        aliments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        aliments = paginator.page(paginator.num_pages)

    # Build the context
    context = {
        'substitutes': aliments,

        'user_request': query,
        'message': message,

        'paginate': True,
    }

    return render(request, 'substitute/search.html', context)


def detail_view(request, aliment_id):
    """
    Display the details of an aliment.
    :param request:
    :param aliment_id:
    :return:
    """

    # Get the aliment from his id
    aliment = Aliment.objects.get(pk=aliment_id)

    print(aliment)
    messages.add_message(request, messages.INFO, 'Hello world.')

    context = {
        'aliment': aliment,
        # 'messages': messages,
    }

    return render(request, 'substitute/details.html', context)


def favorites_view(request):
    """
    Display only the favorites substitutes.
    :param request:
    :return:
    """
    favorite_list =0

    # Ensure that an user is authentified
    if request.user.is_authenticated:
        # Gather a list from database
        favorites_id_list = UserLinkToAlimentsTable.objects.filter(user_id=request.user)
        # Check if we find some elements
        if not favorites_id_list.exists():
            # List is empty
            message = "Misère de misère, vous n'avez encore pas enregistrer de favoris !"
            # Empty list
            favorite_list = []
        else:
            # Some elements are in the list
            message = "Voici vos favoris"
            # Collect the aliments from the list
            favorite_list = []
            for elt in favorites_id_list:
                adrien = Aliment.objects.filter(id=elt.aliment_id).distinct()
                favorite_list.extend(adrien)

    else:
        # User is not identified
        message = "Vous devez etre identifié pour voir vos favoris"

    # Slice page
    paginator = Paginator(favorite_list, 6)
    # Get the current page
    page = request.GET.get('page')

    # Return only this page substitute and not others
    try:
        favorite = paginator.page(page)
        print("Page OK")
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        favorite = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        favorite = paginator.page(paginator.num_pages)

    # Build the context
    context = {
        'substitutes': favorite,
        'message': message,
        'paginate': True,
    }

    return render(request, 'substitute/favorite.html', context)


def save_view(request, aliment_id):
    """
    Save the aliment selected as favorite in the database
    :param request:
    :param aliment_id:
    :return:
    """

    # Add the favorite aliment in the table
    UserLinkToAlimentsTable.objects.create(user_id=request.user, aliment_id=aliment_id)

    messages.success(request, 'Profile details updated.')

    return redirect(request.META['HTTP_REFERER'])


def delete_view(request, aliment_id):
    """
    Remove the aliment selected as favorite in the database
    :param request:
    :param aliment_id:
    :return:
    """

    # Add the favorite aliment in the table
    UserLinkToAlimentsTable.objects.filter(user_id=request.user, aliment_id=aliment_id).delete()

    return redirect(request.META['HTTP_REFERER'])


def initialise_database_view(request):
    """
    Load a few element in database.
    :param request:
    :return:
    """
    # Gather data from API
    api_handler = OpenFoodFactsAPIHandler()
    api_handler.generate_substitutes_dict()

    # Load data in the database
    aliment_table_handler = DataBaseTableHandler(Aliment)
    aliment_table_handler.load_json_file_in_table(api_handler.substitutes_list)

    console_display(aliment_table_handler.message)

    # Content returned
    context = {
        # Return database status
        'message': aliment_table_handler.message,
    }

    return render(request, 'substitute/000.html', context)


def clear_table_view(request):
    """
    Clear the tables
    """

    # Remove data from table
    aliment_table_handler = DataBaseTableHandler(Aliment)
    aliment_table_handler.clear_table()
    favorite_table_handler = DataBaseTableHandler(UserLinkToAlimentsTable)
    favorite_table_handler.clear_table()

    # Console display
    console_display(aliment_table_handler.message)
    console_display(favorite_table_handler.message)

    # Content returned
    context = {
        # Return database status
        'message': aliment_table_handler.message,
    }

    return render(request, 'substitute/000.html', context)
