
import md5
print [x for x in xrange(0,9999999) if md5.new("iwrupvqb" + str(x)).hexdigest()[0:6] == "000000"][0]
