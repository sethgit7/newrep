country={'Australia','Japan','India','China','America'}
games={'hockey','cricket','football','swimming','Australia'}

# print(country)
# country.add('Germany')
# print(country)
#
# country.pop()
# print(country)
#
# country.remove('India')
# print(country)
#
# country.discard('India')
# print(country)
#
# country.update(games)
# print(country)
#
# country.union(games)
# print(country)
#
# country.difference_update(games)
# print(country)

country.symmetric_difference_update(games)
print(country)