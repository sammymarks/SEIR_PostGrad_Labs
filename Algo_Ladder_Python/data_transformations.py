# You are given two parameters, an array and a number. Return a hash whose keys are each of the values from the array parameter, and whose values are the number parameter.

# Input:

# First argument: ["a", "e", "i", "o", "u"]
# Second argument: 1

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }

def ETL_one(lst, num):
    output = {}

    for char in lst:
        output[char] = num

    return output
    
print(ETL_one(["a", "e", "i", "o", "u"], 1))


# Given a hash, return a flat array containing all the hash’s keys and values.

# Input: {“a” => 1, “b” => 2, “c” => 3, “d” => 4}
# Output: [“a”, 1, “b”, 2, “c”, 3, “d”, 4]

def flatten_hash(dict):
    output = []
    # https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/
    for key, val in dict.items():
        output.append(key)
        output.append(val)
    return output

print(flatten_hash({"a" : 1, "b" : 2, "c" : 3, "d" : 4}))


# Given a hash, create a new hash that has the keys and values switched.

# Input: {"a" => 1, "b" => 2, "c" => 3}
# Output: {1 => "a", 2 => "b", 3 => "c"}

def flip_hash(input):
    output = {}
    for key,val in input.items():
        output[val]=key
    return output

print(flip_hash({"a" : 1, "b" : 2, "c" : 3}))

# You are given a hash in format #A, and you are to return the same data as a hash using format #B, as specified below:

# Input:

# {
# 1 => ["A", "E", "I", "O", "U"]
# }

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }
# Input:

# {
# 1 => ["A", "E"],
# 2 => ["D", "G"]
# }

# Output:

# {
# 'a' => 1,
# 'd' => 2,
# 'e' => 1,
# 'g' => 2
# }

# Input:

# {
# 1 => ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
# 2 => ["D", "G"],
# 3 => ["B", "C", "M", "P"],
# 4 => ["F", "H", "V", "W", "Y"],
# 5 => ["K"],
# 8 => ["J", "X"],
# 10 => ["Q", "Z"]
# }

# Output:

# {
# 'a' => 1,
# 'b' => 3,
# 'c' => 3,
# 'd' => 2,
# 'e' => 1,
# 'f' => 4,
# 'g' => 2,
# 'h' => 4,
# 'i' => 1,
# 'j' => 8,
# 'k' => 5,
# 'l' => 1,
# 'm' => 3,
# 'n' => 1,
# 'o' => 1,
# 'p' => 3,
# 'q' => 10,
# 'r' => 1,
# 's' => 1,
# 't' => 1,
# 'u' => 1,
# 'v' => 4,
# 'w' => 4,
# 'x' => 8,
# 'y' => 4,
# 'z' => 10
# }

def ETL_two(input):
    output = {}
    
    for key, val in input.items():
        for char in val:
            output[char]=key
    return output
    
print(ETL_two(
    {
        1 : ["A", "E", "I", "O", "U"]
    }
))

print(ETL_two(
    {
        1 : ["A", "E"],
        2 : ["D", "G"]
    }
))

print(ETL_two(
{
1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
2 : ["D", "G"],
3 : ["B", "C", "M", "P"],
4 : ["F", "H", "V", "W", "Y"],
5 : ["K"],
8 : ["J", "X"],
10 : ["Q", "Z"]
}
))

# Given an array of social media posts and an array of users, return a list of posts (as an array of hashes) that replaces the submitted_by id number as the person's actual name.

# For example, given this array of posts (note that the submitted_by is an id number):

# [
# {title: 'Me Eating Pizza', submitted_by: 231, likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: 989, likes: 3},
# {title: 'best selfie evar!!!', submitted_by: 111, likes: 1092},
# {title: 'Mondays are the worst', submitted_by: 403, likes: 644}
# ]

# And this array of users:

# [
# {user_id: 403, name: "Aunty Em"},
# {user_id: 231, name: "Joelle P."},
# {user_id: 989, name: "Lyndon Johnson"},
# {user_id: 111, name: "Patti Q."},
# ]

# Return the array of posts as follows:

# [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]

def complete_data_two(posts, users):
    for post in posts:
        result = (list(filter(lambda users: users["user_id"]==post["submitted_by"], users)))
        post["submitted_by"]=result[0]["name"]

    return posts



posts = [
{"title": 'Me Eating Pizza', "submitted_by": 231, "likes": 1549},
{"title": 'i never knew how cool i was until now', "submitted_by": 989, "likes": 3},
{"title": 'best selfie evar!!!', "submitted_by": 111, "likes": 1092},
{"title": 'Mondays are the worst', "submitted_by": 403, "likes": 644}
]

users = [
{"user_id": 403, "name": "Aunty Em"},
{"user_id": 231, "name": "Joelle P."},
{"user_id": 989, "name": "Lyndon Johnson"},
{"user_id": 111, "name": "Patti Q."},
]

print(complete_data_two(posts,users))


# Given a list of books provided in this format:

# [
# {title: "The Lord of the Rings", author: "J. R. R. Tolkien", year: 1954 },
# {title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960 },
# {title: "1984", author: "George Orwell", year: 1949 },
# {title: "Go Set a Watchman", author: "Harper Lee", year: 2015 },
# {title: "The Hobbit", author: "J. R. R. Tolkien", year: 1937 },
# {title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925 },
# {title: "The Two Towers", author: "J. R. R. Tolkien", year: 1954 }
# ]

# return the data in this new author-centric format:

# { "J. R. R. Tolkien" => [
# {title: "The Lord of the Rings", year: 1954 },
# {title: "The Hobbit", year: 1937 },
# {title: "The Two Towers", year: 1954 }
# ],
# "Harper Lee" => [
# {title: "To Kill a Mockingbird", year: 1960 },
# {title: "Go Set a Watchman", year: 2015 }
# ],
# "George Orwell" => [
# {title: "1984", year: 1949 }
# ],
# "F. Scott Fitzgerald" => [
# {title: "The Great Gatsby", year: 1925 }
# ]
# }

def book_organizer(books):
    output = {}
    for book in books:
        if book["author"] not in output.keys():
            output[book["author"]] = [{"title":book["title"], "year":book["year"]}]
        else:
            output[book["author"]] = [*output[book["author"]], {"title":book["title"], "year":book["year"]}]
    return output

print(book_organizer([
{"title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "year": 1954 },
{"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960 },
{"title": "1984", "author": "George Orwell", "year": 1949 },
{"title": "Go Set a Watchman", "author": "Harper Lee", "year": 2015 },
{"title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937 },
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925 },
{"title": "The Two Towers", "author": "J. R. R. Tolkien", "year": 1954 }
]))

# Given an array of Youtube videos, for example:

# [
# {title: 'How to Make Wood', author_id: 4, views: 6},
# {title: 'How to Seem Perfect', author_id: 4, views: 111},
# {title: 'Review of the New "Unbreakable Mug"', author_id: 2, views: 202},
# {title: 'Why Pigs Stink', author_id: 1, views: 12}
# ]

# and an array of authors, for example:

# [
# {id: 1, first_name: 'Jazz', last_name: 'Callahan'},
# {id: 2, first_name: 'Ichabod', last_name: 'Loadbearer'},
# {id: 3, first_name: 'Saron', last_name: 'Kim'},
# {id: 4, first_name: 'Teena', last_name: 'Burgess'},
# ]

# Return a new array of videos in the following format, and only include videos that have at least 100 views:

# [
# {title: 'How to Seem Perfect', views: 111, author_name: 'Teena Burgess' }
# {title: 'Review of the New "Unbreakable Mug"', views: 202, author_name: 'Ichabod Loadbearer' },
# ]

def ETL_three(videos, authors):
    
    output = []

    auths_hash = {}

    # O(N)
    for auth in authors:
        auths_hash[auth["id"]] = auth["first_name"] + " " + auth["last_name"]

    # O(N)
    for vid in videos:
        if vid["views"]>100:
            #O(1) - Free Auths_Hash Lookups
            output.append({"title": vid["title"], "views": vid["views"], "author_name": auths_hash[vid["author_id"]]})

    #O(2N)
    return output

videos = [
{"title": 'How to Make Wood', "author_id": 4, "views": 6},
{"title": 'How to Seem Perfect', "author_id": 4, "views": 111},
{"title": 'Review of the New "Unbreakable Mug"', "author_id": 2, "views": 202},
{"title": 'Why Pigs Stink', "author_id": 1, "views": 12}
]

authors = [
{"id": 1, "first_name": 'Jazz', "last_name": 'Callahan'},
{"id": 2, "first_name": 'Ichabod', "last_name": 'Loadbearer'},
{"id": 3, "first_name": 'Saron', "last_name": 'Kim'},
{"id": 4, "first_name": 'Teena', "last_name": 'Burgess'},
]

print(ETL_three(videos,authors))