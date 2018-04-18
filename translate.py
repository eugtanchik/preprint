from textblob import TextBlob

def preprocess(s):
	s = s.replace('\-', '')
	return s

def postprocess(s):
	s = s.replace(' ~ \ cite ', '~\cite')
	s = s.replace('% ', '%')
	s = s.replace(' ~ \ text ', '~\text')
	s = s.replace('$ ', '$')
	s = s.replace(' $', '$')
	return s

with open('i-ukr.tex', 'r') as f:
	l = f.readline()
	while l:
		print(preprocess(l))
		w = TextBlob(preprocess(l))
		try:
			print(postprocess(w.translate(to='uk')))
		except:
			pass
		l = f.readline()