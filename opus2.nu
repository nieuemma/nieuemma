
def "main" [] {
  print "Handle FLAC and OPUS audio with ease.\n Requires flac, opusenc, and sox.\n Use --help to see available subcommands."
}

def "main encode opus" [bitrate: int, format: string] {
  ls **/*.($format) | each {|file| opusenc $file.name --bitrate $bitrate --picture $"(dirname $file.name)/cover.jpg" ($file.name | str replace .($format) .opus)}

  ls **/*.opus | each {|file| mkdir $"../opus/(dirname $file.name)"; mv $file.name $"../opus/(dirname $file.name)"}
}

def "main encode flac" [format: string] {
  ls **/*.($format) | each {|file| flac -8 $file.name}
}

def "main decode opus" [] {
  ls **/*.opus | each {|file| opusdec $file.name ($file.name | str replace .opus .wav)}

  ls **/*.wav | each {|file| mkdir $"../wav/(dirname $file.name)"; mv $file.name $"../wav/(dirname $file.name)"}
  
}

def "main decode flac" [] {
  ls **/*.flac | each {|file| flac -d $file.name}
  ls **/*.wav | each {|file| mkdir $"../wav/(dirname $file.name)" mv $file.name $"../wav/(dirname $file.name)"}
}

def "main resample" [samplerate: int, format: string] {
  ls **/*.($format) | each {|file| sox $file.name -r $samplerate --guard ($file.name | str replace .($format) _resampled.($format))}
  
}

