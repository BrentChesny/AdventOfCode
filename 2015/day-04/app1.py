
import md5
print [x for x in xrange(0,999999) if md5.new("iwrupvqb" + str(x)).hexdigest()[0:5] == "00000"][0]
