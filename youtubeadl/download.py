import pafy
try:
	url = "https://www.youtube.com/watch?v=2yXfUPwlZTw"
	video = pafy.new(url)
	streams = video.streams
	streams_info=[]

	for ss in streams:
		streams_info.append((ss.resolution,ss.extension,ss.url))

	videInfo = {
		'title' :video.title,
		'author':video.author,
		'streams':streams_info
	}

	print(videoInfo)