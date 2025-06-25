https://www.udemy.com/share/103IHM3@nZ98baJTi_sLLZelYMCV8OdtydZmS5Rnr8NR1EOHtNj3dq59BQ8IUhjbl6t6pLDP_g==/
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year%4 == 0:
        if year%400 == 0 or year%100 != 0:
            return True
        return False
    else:
        return False
