kanto = ["東京都","茨木県","栃木県","群馬県","埼玉県","千葉県","神奈川県"]
print("<select name='area'>")
for area in kanto:
    print("<option>" + area + "</option>")
print("</select>")
