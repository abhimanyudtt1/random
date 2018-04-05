import jaydebeapi
import os

os.environ['CLASSPATH'] = '/Users/abhimanyu.dutta/Downloads/hsqldb-1.8.0.7.jar'
conn = jaydebeapi.connect("org.hsqldb.jdbcDriver",
                          'jdbc:hsqldb:hsql://%s/%s' % ('192.168.113.91', 'rubix35'),
                          ["SA", ""],)
