import hmac
my_hash = hmac.new("happy12345").hexdigest()
print my_hash

# expected: 4441f63125284a43de6e113a7e39bd35
