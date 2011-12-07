import httplib2
import re

def whosampled(number):
    h = httplib2.Http(".cache")
    resp, content = h.request("http://www.whosampled.com/sample/view/"+number+"/")

    #step one is find the title

    rawtitle = re.findall(r'(?<=\<title\>).{1,}(?=|.{1,}\</title\>)',content)[0]
    fullsample = re.findall(r'(?<=sample of ).{1,}', rawtitle)[0]
    fullsong = re.findall(r'.{1,}(?= sample of)', rawtitle)[0]
    
    sampled_artist = re.findall('.*?(?=\&\#39;s)',fullsample)[0]
    sampled_song = re.findall('(?<=\&\#39;s ).{1,}',fullsample)[0]
    artist = re.findall('.*?(?=\&\#39;s)',fullsong)[0]
    song = re.findall('(?<=\&\#39;s ).{1,}',fullsong)[0]
    
    
    sampled_artist=sampled_artist.replace('&#39;','\'')
    sampled_song=sampled_song.replace('&#39;','\'')
    song=song.replace('&#39;','\'')
    sampled_song=sampled_song.split(' |')[0]

    return song, artist, sampled_song, sampled_artist
