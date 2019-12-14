
import math


def parse(f):
	formula = {}
	quants = {}

	# Parse f
	f1 = f.split()
	i = 0
	while i < len(f1):
		requirements = []
		while f1[i] != "=>":
			requirements.append( (f1[i + 1].strip(','), int(f1[i])) )
			i += 2
		i += 1
		formula[f1[i + 1]] = requirements
		quants[f1[i + 1]] = int(f1[i])
		i += 2

	return formula, quants


# Part 1
def get_requirements(formula, quants, fuel):
	
	# Calculate with BFS
	q = [('FUEL', fuel)]
	num_ore = 0
	leftovers = {}
	while len(q) != 0:
		cur_req = q.pop(0)

		if cur_req[0] == 'ORE':
			num_ore += cur_req[1]
			continue

		cur_needed = cur_req[1] - leftovers.get(cur_req[0], 0)
		m_needed = math.ceil( cur_needed / quants[cur_req[0]])

		if cur_needed < 0:
			leftovers[cur_req[0]] = -1 * cur_needed
			cur_needed = 0
			m_needed = 0
		else:
			leftovers[cur_req[0]] = m_needed * quants[cur_req[0]] - cur_needed

		# Push neighbors
		for r in formula[cur_req[0]]:
			q.append((r[0], r[1] * m_needed))

	return num_ore


formula = """1 HVXJL, 1 JHGQ => 2 ZQFQ
6 GRQTX => 6 VZWRS
128 ORE => 2 GRQTX
1 MJPSW => 4 MGZBH
3 HLQX => 8 KSMW
4 QLNS => 9 LFRW
10 HBCN => 3 CZWP
1 CQRJP => 9 MJPSW
1 SLXC => 6 SDTGP
1 MTGVK => 4 NZWLQ
4 PMJX => 3 CVKM
2 LDKGL, 2 SFKF => 5 XZDV
1 QLNS, 1 VZWRS => 5 RSBT
1 NRQS, 22 LQFDM => 4 PMJX
17 XZDV, 8 GSRKQ => 3 ZGDC
11 BPJLM, 18 ZGDC, 1 JHGQ => 5 BXNJX
2 GRQTX, 1 CQRJP => 7 NRQS
1 LJTL => 7 DBHXK
15 HPBQ, 5 PSPCF, 1 JHGQ, 25 ZMXWG, 1 JTZS, 1 SDTGP, 3 NLBM => 6 MQVLS
9 KSMW => 2 GXTBV
3 HVXJL => 5 JHGQ
1 ZWXT, 13 MJPSW, 10 HVXJL => 5 LDKGL
1 GRQTX => 2 LQFDM
190 ORE => 5 FQPNW
1 GTQB => 9 HVHN
1 TNLN, 9 HVHN, 1 WLGT, 4 NZMZ, 2 QTPC, 1 LPTF => 7 WFCH
3 PMJX => 5 SFKF
1 ZGDC => 9 HTVR
193 ORE => 1 CQRJP
1 BPJLM, 1 HPBQ, 3 HVHN => 6 NLBM
2 SFKF => 1 GSRKQ
1 ZGDC => 8 GTQB
1 LSPMR, 53 LDKGL, 24 WFCH, 32 GDLH, 2 HLQX, 14 NLBM, 18 BDZK, 7 MDSRW, 9 MQVLS => 1 FUEL
12 SFKF => 7 NZMZ
13 PVJM => 3 XBTH
7 GSRKQ, 7 LPTF, 1 HLQX, 1 FJHK, 1 DHVM, 3 SFKF, 15 NLBM, 2 SDTGP => 3 LSPMR
4 LFRW, 28 MJPSW => 4 GDLH
6 VZWRS, 8 MJPSW => 8 HVXJL
13 LFRW => 4 ZWQW
1 LQFDM, 7 NZWLQ, 2 HVXJL => 4 HLQX
2 KSMW, 1 WDGN, 4 ZQFQ => 1 ZMXWG
3 MGZBH => 2 LPTF
1 LFRW, 1 CVKM, 3 LDKGL => 4 LJTL
3 LJTL, 20 CZWP, 1 HPBQ => 9 WLGT
3 FQPNW => 8 MTGVK
1 MTDWJ, 1 CVKM => 9 WDGN
5 ZWQW => 3 MTDWJ
2 CVKM => 8 QTPC
2 PVJM, 9 ZWQW, 1 MTDWJ => 4 HBCN
5 RSBT, 2 WDGN, 6 GSRKQ => 1 BPJLM
34 JHGQ, 6 ZGDC => 8 DHVM
3 QTPC, 1 RSBT, 1 GXTBV => 9 JTZS
1 BXNJX, 2 JTZS => 5 SLXC
23 LPTF, 2 NZMZ => 4 TNLN
24 HTVR, 5 DBHXK => 2 FJHK
5 LPTF, 5 QTPC => 4 PSPCF
17 MTGVK, 27 LQFDM => 4 QLNS
1 CVKM, 5 HTVR => 8 HPBQ
6 ZQFQ, 28 XBTH => 7 MDSRW
13 WDGN => 5 BDZK
1 MJPSW, 2 VZWRS => 4 ZWXT
1 MGZBH, 1 GRQTX => 8 PVJM"""


def main():
	f, q = parse(formula)

	# Part 1
	print(get_requirements(f, q, 1))

	# Part2 (This would have taken forver without the below trick)
	i = 0
	multiple = 1000000
	answer = 0
	prev_answer = 0
	while answer < 1000000000000:
		prev_answer = answer
		answer = get_requirements(f, q, i)
		if answer > 1000000000000:
			answer = prev_answer
			i -= multiple
			multiple = multiple // 10
			if multiple == 0:
				break
		print(answer, i)
		#print(i)
		i += multiple
	print(i)


if __name__ == "__main__":
	main()
