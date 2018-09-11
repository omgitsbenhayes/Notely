from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render
from couchdb import Server
from couchdb.http import ResourceNotFound
from datetime import datetime
from collections import defaultdict

SERVER = Server('http://localhost:5984')

def index(request):
  db = SERVER['notely']
  notes = []
  for doc in db:
    note = {}
    note['id'] = db[doc]['_id']
    note['title'] = db[doc]['title']
    note['text'] = db[doc]['text']
    note['tags'] = db[doc]['tags'].split()
    note['editdate'] = datetime.strptime(db[doc]['editdate'], '%Y-%m-%d %H:%M')
    note['createdate'] = db[doc]['createdate']
    notes.append(note)
  return render(request, 'notes/index.html',{'rows':notes})

def detail(request,id):
  db = SERVER['notely']
  try:
    note = db[id]
  except ResourceNotFound:
    raise Http404
  if request.method == "POST":
    note['title'] = request.POST['title']
    note['text'] = request.POST['text']
    note['tags'] = request.POST['tags']
    note['editdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    note['createdate'] = note['createdate']
    db[id] = note
  note['tags2'] = db[id]['tags'].split()
  note['editdate'] = datetime.strptime(db[id]['editdate'], '%Y-%m-%d %H:%M')
  return render(request, 'notes/detail.html',{'row':note})

def create(request):
  db = SERVER['notely']
  if request.method == "POST":
    note = {}
    note['title'] = request.POST['title']
    note['text'] = request.POST['text']
    note['tags'] = request.POST['tags']
    note['editdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    note['createdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    id = note['title'].replace(' ','_')
    db[id] = note
    return HttpResponseRedirect(u"/notely/note/%s/" % id)
  return render(request, 'notes/create.html')

def tag(request,q):
  db = SERVER['notely']

  notes = []
  for doc in db:
    if q.upper() in db[doc]['tags'].upper():
      note = {} 
      note['id'] = db[doc]['_id']
      note['title'] = db[doc]['title']
      note['text'] = db[doc]['text']
      note['tags'] = db[doc]['tags'].split()
      note['editdate'] = datetime.strptime(db[doc]['editdate'], '%Y-%m-%d %H:%M')
      note['createdate'] = db[doc]['createdate']
      notes.append(note)
  return render(request, 'notes/tag.html',{'rows':notes})
