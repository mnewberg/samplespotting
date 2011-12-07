from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response
import breaks
import urllib
import re
from django.utils import simplejson

def index(request):
    return render_to_response('search_form.html')

def search(request):
    if request.method=='GET':
        #xhr = request.GET.has_key('xhr')
        # file('/tmp/log', 'a+').write(str(request.GET.get('q')))
        if request.GET['q'].startswith('http://open.spotify.com/local/'):
            return HttpResponse(simplejson.dumps({'Localerror':'Local error'}), mimetype='application/javascript') 
        else:
            pass
        artist, song = breaks.input(request.GET['q'])
        output = breaks.func(song, artist)  

        results = []
        for item in output:
            results.append(breaks.spotify(output[item][0]+' '+item))

        if len(results) > 0:
           # if results[0]!=None:
            for index, key in enumerate(output.iterkeys()):
                    output[key]=results[index],output[key][0]
            
            return HttpResponse(simplejson.dumps({'query':request.GET['q'][30:],'output':output, 'song':song, 'artist':artist, 'sample_artist':output[item][1], 'sample_song':item}), mimetype='application/javascript')
           # elif results[0]==None:
               # return HttpResponse(simplejson.dumps({'spotify_error':True,'sampled_song':item, 'sampled_artist':output[item][0]}), mimetype='application/javascript')
        else:
            return HttpResponse(simplejson.dumps({'Error':'Can\'t find a sample', 'song':song}), mimetype='application/javascript')
       
def song(request, id):
    #xhr = request.GET.has_key('xhr')
    # file('/tmp/log', 'a+').write(str(request.GET.get('q')))
    daquery='http://open.spotify.com/track/'+ id
    artist, song = breaks.input(daquery)
    output = breaks.func(song, artist)  
    results = []
    for item in output:
        results.append(breaks.spotify(output[item][0]+' '+item))
    for index, key in enumerate(output.iterkeys()):
        output[key]=results[index],output[key][0]
    return render_to_response('callback.html',{'output':output.iteritems(), 'results':results, 'song':song, 'artist':artist})
