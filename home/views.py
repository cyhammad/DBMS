from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import *
from datetime import datetime
from django.contrib import messages
from PIL import Image
from pathlib import Path



# Create your views here.

context = { 
        "username": "none"
        };

def imageConverter():
    im = Image.open("")
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im, (0,0), im)
    bg.save("","",quality= 95)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username");
        password = request.POST.get("password");

        user = User.objects.get(username = username);
        if (user.password == password):
            context["username"] = username
            return render(request,'index.html', context);
        else:
            messages.warning(request, "Invalid username/password")

    return render(request, 'login.html');


def index(request):
    if context["username"] == "none":
        return render(request, 'login.html');
    return render(request,'index.html', context);

def library(request):
    if context["username"] == "none":
        return render(request, 'login.html');
    gameList = Game.objects.all();
    if request.method == "POST":
        searchedGame = request.POST.get("searchedGame")
        gameList = gameList.filter(name = searchedGame)
    
    context["games"] = gameList
    return render(request, 'library.html', context);

def community(request):
    if context["username"] == "none":
        return render(request, 'login.html');
    return render(request, 'community.html',context);

def advanceSearch(request):
    context["selectedCategory"] = context["selectedGenre"] = context["selectedYear"] = context["selectedRating"] = context["searchGames"] = "All"
    searchedGameList = Game.objects.all()

    if context["username"] == "none":
        return render(request, 'login.html');

    genreList = Genre.objects.all()
    context["genres"] = genreList

    categoryList = Category.objects.all()
    context["categories"] = categoryList

    yearList = []
    for x in range(2000, 2021):
        yearList.append(x)
    context["years"] = yearList

    ratingList = []
    for y in range(9,0,-1):
        ratingList.append(y)
    context["ratings"] = ratingList
    
    if request.method == "POST":
        selectedCategory = request.POST.get("categoryOpt")
        selectedGenre = request.POST.get("genreOpt")
        selectedYear = request.POST.get("yearOpt")
        selectedRating = request.POST.get("ratingOpt")

        if selectedCategory == "All":
            pass
        else:
            categoryObj = categoryList.get(name = selectedCategory)
            searchedGameList = searchedGameList.filter(category = categoryObj)
        
        if selectedGenre == "All":
            pass
        else:
            genreObj = genreList.get(name = selectedGenre)
            searchedGameList = searchedGameList.filter(genre = genreObj)
        
        if selectedYear == "All":
            pass
        else:
            searchedGameList = searchedGameList.filter(releaseYear__gte = selectedYear)
        
        if selectedRating == "All":
            pass
        else:
            searchedGameList = searchedGameList.filter(ratings__gte = selectedRating)
        
        # searchedGameList = gameList.filter(category = categoryObj, genre = genreObj, releaseYear__gte = selectedYear, ratings__gte = selectedRating)
        context["selectedCategory"] = selectedCategory
        context["selectedGenre"] = selectedGenre
        context["selectedYear"] = selectedYear
        context["selectedRating"] = selectedRating 

    context["gameCount"] = len(searchedGameList)
    context["searchGames"] = searchedGameList
    return render(request, 'advanceSearchHome.html', context)

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username");
        password = request.POST.get("password");
        retypePassword = request.POST.get("retypepassword")
        email = request.POST.get("email");
        phone = request.POST.get("phone");
        if password == retypePassword:
            newUser = User(username = username, password = password, email = email, phone = phone, creationDate = datetime.today());
            newUser.save();
            messages.success(request, 'User created.')
        else:
            messages.warning(request, 'Confirm password is different from password!')

    return render(request, 'signup.html');



def addgame(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        releaseYear = request.POST.get("releaseYear")
        ratings = request.POST.get("ratings")
        newGame = Game(name = name, description = description, releaseYear = releaseYear, ratings = ratings)
        newGame.save()
        messages.success(request, 'Game Saved!')

    return render(request,'addgame.html', context)

def game(request,name):
    if request.method == "POST":
        if context["username"] == "none":
            messages.warning(request, 'You must log in to post a review')    
        else:
            reviewer = User.objects.get(username = context["username"])
            ofGame = Game.objects.get(name = name)
            reviewTitle = request.POST.get("reviewTitle");
            comment = request.POST.get("comment");
            newReview = Review(reviewer = reviewer,ofGame = ofGame ,title =reviewTitle,comment = comment);
            newReview.save();
            messages.success(request, 'Review Posted!')

    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    context["name"] = name
    context["description"] = gameObj.description
    context["releaseYear"] = gameObj.releaseYear
    context["ratings"]= gameObj.ratings
    context["price"] = gameObj.price

    genres = gameObj.genre.all()
    genreList = []
    for genre in genres:
        genreList.append(genre.name)
    context["genres"] = genreList

    categories = gameObj.category.all()
    categoryList = []
    for category in categories:
        categoryList.append(category.name)
    context["categories"] = categoryList

    reviewList = Review.objects.filter(ofGame=gameObj)

    context["reviewList"] = reviewList

    return render(request, "details.html",context);

def tournaments(request,name):
    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    tournamentList = Tournament.objects.all().filter(ofGame = gameObj)
    
    context["tournaments"] = tournamentList

    return render(request, "tournaments.html", context)

def proPlayers(request,name):
    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    playerList = ProPlayer.objects.all().filter(ofGame = gameObj)
    
    context["proPlayers"] = playerList

    return render(request, "proplayers.html", context)
    
def proTeams(request,name):
    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    teamList = ProTeam.objects.all().filter(ofGame = gameObj)
    
    context["proTeams"] = teamList

    return render(request, "proteams.html", context)

def developers(request,name):
    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    developerList = gameObj.developer.all()
    
    context["developers"] = developerList

    return render(request, "developers.html", context)

def news(request,name):
    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    newsList = News.objects.all().filter(ofGame = gameObj)
    
    context["news"] = newsList

    return render(request, "news.html", context)

def updates(request,name):
    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    updateList = Update.objects.all().filter(ofGame = gameObj)
    
    context["updates"] = updateList

    return render(request, "updates.html", context)

def awards(request,name):
    gameList = Game.objects.all()
    gameObj = gameList.get(name = name)
    awardList = Award.objects.all().filter(winner = gameObj)
    
    context["awards"] = awardList

    return render(request, "awards.html", context)
