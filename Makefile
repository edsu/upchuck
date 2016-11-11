all: hydrate
	./congrats.py > congrats.csv

hydrate: 
	@if [ ! -f "tweets.json" ]; then \
	    twarc.py --hydrate ids.txt > tweets.json;\
	fi
 


