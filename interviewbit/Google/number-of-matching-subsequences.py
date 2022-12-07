import bisect
import time
from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexMap = defaultdict(list)
        for i, c in enumerate(s):
            indexMap[c].append(i)

        total = 0
        for word in words:
            i, j = -1, 0
            for j, c in enumerate(word):
                if c not in indexMap:
                    break
                k = bisect.bisect_right(indexMap[c], i)
                if k == len(indexMap[c]) or indexMap[c][k] < i:
                    break
                i = indexMap[c][k]
            if j == len(word) - 1:
                total += 1
        return total

    def numMatchingSubseq12(self, s: str, words: List[str]) -> int:
        indexMap = defaultdict(list)
        for i, c in enumerate(s):
            indexMap[c].append(i)

        total = 0
        for word in words:
            i, j, found = -1, 0, False
            k, c = 0, ""
            for j, c in enumerate(word):
                if c not in indexMap:
                    break
                k = bisect.bisect_right(indexMap[c], i)
                if k == len(indexMap[c]) or indexMap[c][k] < i:
                    break
                i = indexMap[c][k]
            if j == len(word) - 1 and k < len(indexMap[c]) and indexMap[c][k] == i:
                total += 1
        return total

    def numMatchingSubseq2(self, s: str, words: List[str]) -> int:
        indexMap = defaultdict(list)
        for i, c in enumerate(s):
            indexMap[c].append(i)

        total = 0
        for word in words:
            i, found = -1, True
            for c in word:
                j = i
                if c not in indexMap:
                    found = False
                    break
                for k in indexMap[c]:
                    if k > i:
                        i = k
                        break
                if i == j:
                    found = False
                    break
            if c in indexMap and (
                    (j == len(word) - 2 and word[-1] in indexMap and indexMap[word[-1]][-1] > i) or len(word) == 1):
                total += 1
        return total

    def numMatchingSubseq3(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

    def numMatchingSubseq4(self, s: str, words: List[str]) -> (int, List[str]):
        waiting = defaultdict(list)
        for i, w in enumerate(words):
            waiting[w[0]].append((i, 1))
        ans = []
        res = 0
        for k, c in enumerate(s):
            for i, j in waiting.pop(c, ()):
                if j >= (len(words[i]) - 1):
                    ans.append(words[i])
                    res += 1
                    continue
                waiting[words[i][j]].append((i, j + 1))

        return res, sorted(ans)


s = "abcde"
words = ["a", "bb", "acd", "ace"]
s = "ricogwqznwxxcpueelcobbbkuvxxrvgyehsudccpsnuxpcqobtvwkuvsubiidjtccoqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjscnlhbrhookmioxqighkxfugpeekgtdofwzemelpyjsdeeppapjoliqlhbrbghqjezzaxuwyrbczodtrhsvnaxhcjiyiphbglyolnswlvtlbmkrsurrcsgdzutwgjofowhryrubnxkahocqjzwwagqidjhwbunvlchojtbvnzdzqpvrazfcxtvhkruvuturdicnucvndigovkzrqiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqnhrewhagldzhryzdmmrwnxhaqfezeeabuacyswollycgiowuuudrgzmwnxaezuqlsfvchjfloczlwbefksxsbanrektvibbwxnokzkhndmdhweyeycamjeplecewpnpbshhidnzwopdjuwbecarkgapyjfgmanuavzrxricbgagblomyseyvoeurekqjyljosvbneofjzxtaizjypbcxnbfeibrfjwyjqrisuybfxpvqywqjdlyznmojdhbeomyjqptltpugzceyzenflfnhrptuugyfsghluythksqhmxlmggtcbdddeoincygycdpehteiugqbptyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjckmaptilrbfpjxiarmwalhbdjiwbaknvcqovwcqiekzfskpbhgxpyomekqvzpqyirelpadooxjhsyxjkfqavbaoqqvvknqryhotjritrkvdveyapjfsfzenfpuazdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzqfgqwhgobwyhxltligahroyshfndydvffd"
words = ["iowuuudrgzmw", "azfcxtvhkruvuturdicnucvndigovkzrq", "ylmmo", "maptilrbfpjxiarmwalhbd",
         "oqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqgl", "ytldcdlxqbaszbuxsacqwqnhrewhagldzhr", "zeeab", "cqie",
         "pvrazfcxtvhkruvuturdicnucvndigovkzrqiya", "zxnvpluwicurrtshyvevkriudayyysepzq", "wyhxltligahroyshfn",
         "nhrewhagldzhryzdmmrwn", "yqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmw", "nhrptuugyfsghluythksqhmxlmggtcbdd",
         "yligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjsc", "zdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzq",
         "ncygycdpehteiugqbptyqbvokpwovbnplshnzafun", "gdzutwgjofowhryrubnxkahocqjzww", "eppapjoliqlhbrbgh",
         "qwhgobwyhxltligahroys", "dzutwgjofowhryrubnxkah", "rydhxkdhffyytldcdlxqbaszbuxs",
         "tyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjc", "khvyjyrydhxkdhffyytldcdlxqbasz",
         "jajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqn", "ppapjoliqlhbrbghq", "zmwwxzjckmaptilrbfpjxiarm",
         "nxkahocqjzwwagqidjhwbunvlchoj", "ybfxpvqywqjdlyznmojdhbeomyjqptltp", "udrgzmwnxae", "nqglnpjvwddvdlmjjyzmww",
         "swlvtlbmkrsurrcsgdzutwgjofowhryrubn", "hudqbfnzxnvpluwicurr", "xaezuqlsfvchjf",
         "tvibbwxnokzkhndmdhweyeycamjeplec", "olnswlvtlbmkrsurrcsgdzu", "qiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyyt",
         "eiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwyl", "cgiowuuudrgzmwnxaezuqlsfvchjflocz", "rxric",
         "cygycdpehteiugqbptyqbvokpwovbnplshnzaf", "g", "surrcsgd", "yzenflfnhrptuugyfsghluythksqh",
         "gdzutwgjofowhryrubnxkahocqjzwwagqid", "ddeoincygycdpeh", "yznmojdhbeomyjqptltpugzceyzenflfnhrptuug",
         "ejuisks", "teiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoi", "mrwnxhaqfezeeabuacyswollycgio",
         "qfskkpfakjretogrokmxemjjbvgmmqrfdxlkfvycwalbdeumav", "wjgjhlrpvhqozvvkifhftnfqcfjmmzhtxsoqbeduqmnpvimagq",
         "ibxhtobuolmllbasaxlanjgalgmbjuxmqpadllryaobcucdeqc", "ydlddogzvzttizzzjohfsenatvbpngarutztgdqczkzoenbxzv",
         "rmsakibpprdrttycxglfgtjlifznnnlkgjqseguijfctrcahbb", "pqquuarnoybphojyoyizhuyjfgwdlzcmkdbdqzatgmabhnpuyh",
         "akposmzwykwrenlcrqwrrvsfqxzohrramdajwzlseguupjfzvd", "vyldyqpvmnoemzeyxslcoysqfpvvotenkmehqvopynllvwhxzr",
         "ysyskgrbolixwmffygycvgewxqnxvjsfefpmxrtsqsvpowoctw", "oqjgumitldivceezxgoiwjgozfqcnkergctffspdxdbnmvjago",
         "bpfgqhlkvevfazcmpdqakonkudniuobhqzypqlyocjdngltywn", "ttucplgotbiceepzfxdebvluioeeitzmesmoxliuwqsftfmvlg",
         "xhkklcwblyjmdyhfscmeffmmerxdioseybombzxjatkkltrvzq", "qkvvbrgbzzfhzizulssaxupyqwniqradvkjivedckjrinrlxgi",
         "itjudnlqncbspswkbcwldkwujlshwsgziontsobirsvskmjbrq", "nmfgxfeqgqefxqivxtdrxeelsucufkhivijmzgioxioosmdpwx",
         "ihygxkykuczvyokuveuchermxceexajilpkcxjjnwmdbwnxccl", "etvcfbmadfxlprevjjnojxwonnnwjnamgrfwohgyhievupsdqd",
         "ngskodiaxeswtqvjaqyulpedaqcchcuktfjlzyvddfeblnczmh", "vnmntdvhaxqltluzwwwwrbpqwahebgtmhivtkadczpzabgcjzx",
         "yjqqdvoxxxjbrccoaqqspqlsnxcnderaewsaqpkigtiqoqopth", "wdytqvztzbdzffllbxexxughdvetajclynypnzaokqizfxqrjl",
         "yvvwkphuzosvvntckxkmvuflrubigexkivyzzaimkxvqitpixo", "lkdgtxmbgsenzmrlccmsunaezbausnsszryztfhjtezssttmsr",
         "idyybesughzyzfdiibylnkkdeatqjjqqjbertrcactapbcarzb", "ujiajnirancrfdvrfardygbcnzkqsvujkhcegdfibtcuxzbpds",
         "jjtkmalhmrknaasskjnixzwjgvusbozslrribgazdhaylaxobj", "nizuzttgartfxiwcsqchizlxvvnebqdtkmghtcyzjmgyzszwgi",
         "egtvislckyltpfogtvfbtxbsssuwvjcduxjnjuvnqyiykvmrxl", "ozvzwalcvaobxbicbwjrububyxlmfcokdxcrkvuehbnokkzala",
         "azhukctuheiwghkalboxfnuofwopsrutamthzyzlzkrlsefwcz", "yhvjjzsxlescylsnvmcxzcrrzgfhbsdsvdfcykwifzjcjjbmmu",
         "tspdebnuhrgnmhhuplbzvpkkhfpeilbwkkbgfjiuwrdmkftphk", "jvnbeqzaxecwxspuxhrngmvnkvulmgobvsnqyxdplrnnwfhfqq",
         "bcbkgwpfmmqwmzjgmflichzhrjdjxbcescfijfztpxpxvbzjch", "bdrkibtxygyicjcfnzigghdekmgoybvfwshxqnjlctcdkiunob",
         "koctqrqvfftflwsvssnokdotgtxalgegscyeotcrvyywmzescq", "boigqjvosgxpsnklxdjaxtrhqlyvanuvnpldmoknmzugnubfoa",
         "jjtxbxyazxldpnbxzgslgguvgyevyliywihuqottxuyowrwfar", "zqsacrwcysmkfbpzxoaszgqqsvqglnblmxhxtjqmnectaxntvb",
         "izcakfitdhgujdborjuhtwubqcoppsgkqtqoqyswjfldsbfcct", "rroiqffqzenlerchkvmjsbmoybisjafcdzgeppyhojoggdlpzq",
         "xwjqfobmmqomhczwufwlesolvmbtvpdxejzslxrvnijhvevxmc", "ccrubahioyaxuwzloyhqyluwoknxnydbedenrccljoydfxwaxy",
         "jjoeiuncnvixvhhynaxbkmlurwxcpukredieqlilgkupminjaj", "pdbsbjnrqzrbmewmdkqqhcpzielskcazuliiatmvhcaksrusae",
         "nizbnxpqbzsihakkadsbtgxovyuebgtzvrvbowxllkzevktkuu", "hklskdbopqjwdrefpgoxaoxzevpdaiubejuaxxbrhzbamdznrr",
         "uccnuegvmkqtagudujuildlwefbyoywypakjrhiibrxdmsspjl", "awinuyoppufjxgqvcddleqdhbkmolxqyvsqprnwcoehpturicf"]

s = "abcde"
words = ["a","bb","acd","ace"]
test = Solution()
print(test.numMatchingSubseq(s, words))
t0 = time.time()
# print(test.numMatchingSubseq3(s, words))
t1 = time.time()
print(test.numMatchingSubseq12(s, words))
t2 = time.time()

print(t1-t0)
print(t2 - t1)
