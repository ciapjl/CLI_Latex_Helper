import re


integral_description = 'indicate that your wish for a integral to be process. The option is to add the lower and upper limits to your integral by using the one of the following characters: ;,:- to delineate the lower and upper bounds'


def processIntegralBounds(bounds):
    limits = ""
    if bounds != "":
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
        containsDifferential = re.search("d.*$", integrand) != None
        containsVariableofIntegral =  re.search('[a-zA-Z]', integrand) != None
        
        if containsVariableofIntegral and not containsDifferential :
            ##add relevant d{variableofIntegration} if missing and it exists
            variableWRT = re.findall('[a-zA-Z]', integrand)[0]
            finalIntegrand = f"{integrand} \ d{variableWRT}"
        elif not (containsDifferential or containsVariableofIntegral):
            #use t as the variable of integration if integrand comprises of constants and no differential is present
            finalIntegrand = f"{integrand} \ dt"
        elif containsDifferential and containsVariableofIntegral:
            differential = re.search("d.*$", integrand)[0]
            integrandWithoutDifferential  = integrand[:integrand.index(differential[0])].strip()
            finalIntegrand = f"{integrandWithoutDifferential} \ {differential}"

    return finalIntegrand




def processIntegral(input, integral_bounds):
    """This function servers to process integrals """
    boundsProcessed = processIntegralBounds(integral_bounds)
    integrandProcess = processIntegrand(input)
    return f"\[\int{{{boundsProcessed}}}{{{integrandProcess}}}\]"





