import re
import httplib2
import spotimeta

def func(searchterm, daartist):
    searchterm = re.sub(r'\s','+', searchterm)
    h = httplib2.Http("/tmp/cache")
    resp, content = h.request("http://the-breaks.com/search.php?term="+searchterm+"&type=7")
    artists = re.findall(r'(?<=\<b\>).{1,}(?=\</b\>)',content)
    songs = re.findall(r'(?<=\*\s").{1,}(?=")',content)
    sampling_artist = re.findall(r'(?<=&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;).{1,}(?=\s-)',content)
    coords = []
    store= []
    # determine where there are two or more songs per sampled artist
    location = re.finditer(r'(?<=\<b\>).{1,}(?=\</b\>)',content)
    for match in location:
        coords.append(match.span())
    coords.append((len(content),len(content)))
    for n in range (0,len(coords)-1,1):
        start,end = coords[n][0],coords[n+1][0]
        dasearch = re.findall(r'\*',content[start:end])
        if len(dasearch)>1:
            for x in (0,len(dasearch)):
                store.append(n)
    # make correction for the multiple tracks per sampling artist
    counter=0       
    for item in store:
        artists.insert(item+counter,artists[item+counter])
        counter += 1
    # create dict for output        
    bundle={}
    n=0        
    for song in songs:
        criteria = re.sub(r'\s','|(?i)', daartist)
        if len(re.findall(r'(?i)'+criteria, sampling_artist[n]))>=1:            
            bundle[song]=artists[n],sampling_artist[n]
            n+=1
        else:
            n+=1
    return bundle
    
def spotify(query):
    search = spotimeta.search_track(query)
    if search['total_results']>0:
        return search['result'][0]['href']
    else:
        return None 
        
            
def input(URL):
    track=spotimeta.lookup(URL)
    song=re.sub(r'Explicit|Dirty|Theme|LP|\'|Version|-|\(.{1,}\)|Soundtrack|Clean|Edited|Album','', track['result']['name'])
    artist=re.sub(r'The|,','',track['result']['artist']['name'])
    return artist, song
    
 
