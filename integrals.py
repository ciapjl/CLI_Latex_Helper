


integral_description = 'add the lower and upper limits to your integral by using a space or comma to delimiter the boundaries'


def processIntegral(s, a="", b=""):
    limits = f"_{{{a}}}^{{{b}}}"
    return f"\[\int{limits}{s}\]"
