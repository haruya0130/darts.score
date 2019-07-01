import json

def main():
    f = open("myu_s.json".'r')
    json_data = json.load(f)
    name_list = name_list = ["honoka","eri","kotori","umi","rin","maki","nozomi","hanayo","niko"]
    for name in name_list:
        print("{0:6s} 身長：{1}cm BWH: ".format(name,json_data[name]["height"]),end="\t")
        for i in range(len(json_data[name]["BWH"])):
            print("{}".format(json_data[name]["BWH"][i]),end="\t")
        print()

if __name__=='__main__':
    main()



