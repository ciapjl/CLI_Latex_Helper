import re


integral_description = 'add the lower and upper limits to your integral by using the one of the following characters: ;,:- '


def processIntegralBounds(bounds):
    limits = ""
    if bounds != "":
        bounds_array = re.split("[, *;-:|]", bounds)
        bounds_array = list(filter(lambda x: x !='', bounds_array))
        if len(bounds_array)<1:
            limits=f"_{{{bounds_array[0]}}}"
        else:
            limits = f"_{{{bounds_array[0]}}}^{{{bounds_array[1]}}}"   
    return limits

    

    


def processIntegrand(integrand):
    finalIntegrand = ""
    if integrand != "":
        if not re.search("d*$", integrand) and re.search('[a-zA-Z]', integrand):
            ##add relevant dx if missing when
            varaibleWRT = re.findall('[a-zA-Z]', integrand)[0]
            finalIntegrand = f"{integrand}dx"
        elif not re.search("d*$", integrand):
            #use t as the variable of integration if integrand comprises of constants
            finalIntegrand = f"{integrand}dt"
        else:
            finalIntegrand = integrand 

    return finalIntegrand




def processIntegral(input, integral_bounds):
    """This function servers to process integrals """
    boundsProcessed = processIntegralBounds(integral_bounds)
    integrandProcess = processIntegrand(input)
    return f"\[\int{boundsProcessed}{processIntegrand}\]"





