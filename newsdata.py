#!/usr/bin/env python3
import psycopg2


# What are the most popular three articles of all time?
queryTitle1 = ("What are the most popular three articles of all time?")
query1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

# Who are the most popular article authors of all time?
queryTitle2 = ("Who are the most popular article authors of all time?")
query2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

# On which days did more than 1% of requests lead to errors
queryTitle3 = ("On which days did more than 1% of requests lead to errors?")
query3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def connect(database_name="news"):
    """Connecting PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


def getQueryResults(query):
    """Return query results for given query """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def printQueryResults(queryResults):
    print (queryResults[1])
    for index, results in enumerate(queryResults[0]):
        print (
            "\t", index+1, "-", results[0],
            "\t - ", str(results[1]), "views")


def printErrorResults(queryResults):
    print (queryResults[1])
    for results in queryResults[0]:
        print ("\t", results[0], "-", str(results[1]) + "% errors")


if __name__ == '__main__':
    # store query results
    popularArticlesResults = getQueryResults(query1), queryTitle1
    popularAuthorsResults = getQueryResults(query2), queryTitle2
    loadErrorDays = getQueryResults(query3), queryTitle3

    # print query results
    printQueryResults(popularArticlesResults)
    printQueryResults(popularAuthorsResults)
    printErrorResults(loadErrorDays)
