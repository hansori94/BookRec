##March 29, merging two json files into one! 
##
##	Let's make it a name convention that the data we get from using a method with review.show API call to be 
##	r_1_10000.json (review ID from 1 to 10000), for example.
##	AND for data from calling book.show API call to be called
## 	b_1_1000.json  (book ID from 1 to 1000).

##	This will make it easy for everyone to call this script.

import time
import json



def merge_json_to_new_file(src, add, target):



	src_file = open("{}.json".format(src), "r")
	src_json_string = src_file.read()
	src_dict = json.loads(src_json_string)
	
	add_file = open("{}.json".format(add), "r")
	add_json_string = add_file.read()
	add_dict = json.loads(add_json_string)

	#number of books in the src_file
	num_books_prev = len(src_dict)

	####test 1####
	old_book_list = []

	#adding add file to src file! make sure src file is the larger file
	#to make it faster.
	for book_title in add_dict:
		reviews_to_be_added = add_dict[book_title]['review']
		#it's an empty review, so we will skip this iteration.
		if reviews_to_be_added[0] == '\n  ': continue 
 		if book_title in src_dict:
 			####test 1####
 			old_book_list.append(book_title)
			src_reviews = src_dict[book_title]['review']
			add_reviews = add_dict[book_title]['review']
			for review in add_reviews:
				src_reviews.append(review)
			src_dict[book_title]['review'] = src_reviews
		else:
			#a new book is found! copy over the whole book dictionary.
			src_dict[book_title] = add_dict[book_title]

	#number of books in the src_file + add_file = target_file
	num_books_curr = len(src_dict)

	with open("{}.json".format(target), "w") as target_file:
		json.dump(src_dict, target_file)
	
	#no need to close the target_file
	src_file.close()
	add_file.close()    

	return (num_books_prev, num_books_curr, old_book_list)

if __name__ == "__main__":
	start = time.time()
	############################################
	src = raw_input("\nEnter the name of the larger file (excluding .json) \nEx. for r_1_200.json, type in r_1_200 \ninput : ")
	add = raw_input("\nEnter the name of the smaller file (excluding .json) \nEx. for r_201_250.json, type in r_201_250 \ninput : ")
	target = raw_input("\nEnter the name of the target file (excluding .json): ") 
	# src = "1_200"
	# add = "201_400"
	# target = "1_400"
	result = merge_json_to_new_file(src, add, target)
	print("\nThere were {} books before.".format(result[0]))
	print("\nThere are {} books now.".format(result[1]))
	####test 1####
	print("\nThe books that were shared by both files are {}.".format(result[2]))
	############################################
	end = time.time()
	elapsed_time = end - start
	print("ran in {} seconds".format(elapsed_time))

