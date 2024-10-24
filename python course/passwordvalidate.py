pattern= re.compile(r"#([A-Za-z0-9$%#@]{7,}[0-9])")
string="Advay"
pattern2= re.compile
password= "hjkl"

a= pattern.search(string)
check= pattern2.fullmatch(password)
print(check)

