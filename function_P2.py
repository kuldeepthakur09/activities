'''Write a function that allows a message with only 30 words.'''


def msg_length(msg):
    if len(msg) <= 200:
        return msg
    else:
        return msg[:200]

message = "Hello, how are you? I hope you're doing well. Just wanted to check in and see how things are going with you. Let's catch up soon!"
restricted_message = msg_length(message)

print(restricted_message)


def word_count(msg):
    words = msg.split()
    if len(words) <= 30:
        return msg
    else:
        new_msg = ""
        for i in range(30):
            new_msg += words[i]
            if i < 29:
                new_msg += " "
        return new_msg
message = "Hello, how are you? I hope you're doing well. Just wanted to check in and see how things are going with you. Let's catch up soon!"
_msg = word_count(message)

print(_msg)