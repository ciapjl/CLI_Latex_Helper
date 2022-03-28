import re


integral_description = 'indicate that your wish for a integral to be process. The option is to add the lower and upper limits to your integral by using the one of the following characters: ;,:- to delineate the lower and upper bounds'


def processIntegralBounds(bounds):
    limits = ""
    if bounds != "":
        if '-' in bounds:
            bounds_array = bounds.split('-')
        else: 
            bounds_array = re.split("[,;*| ]", bounds)
        bounds_array = list(filter(lambda x: x !='', bounds_array))
        if len(bounds_array)<1:
            limits=f"_{{{bounds_array[0]}}}"
        else:
            limits = f"_{{{bounds_array[0]}}}^{{{bounds_array[1]}}}"   
    return limits
    
    

    


def processIntegrand(integrand):
    finalIntegrand = ""
    if integrand != "":
        if re.search("d*$", integrand) != None and re.search('[a-zA-Z]', integrand) != None:
            ##add relevant dx if missing when
            variableWRT = re.findall('[a-zA-Z]', integrand)[0]
            finalIntegrand = f"{integrand} \ d{variableWRT}"
        elif re.search("d*$", integrand) != None:
            #use t as the variable of integration if integrand comprises of constants
            finalIntegrand = f"{integrand} \ dt"
        else:
            finalIntegrand = integrand 

    return finalIntegrand




def processIntegral(input, integral_bounds):
    """This function servers to process integrals """
    boundsProcessed = processIntegralBounds(integral_bounds)
    integrandProcess = processIntegrand(input)
    return f"\[\int{{{boundsProcessed}}}{{{integrandProcess}}}\]"





