def max(self, m2):
    NRows = min(self.NRows, len(data))
    NCols = min(self.NCols, len(data[0]))
    data = [[0] * NCols for r in range(NRows)]
    for i in range(NRows):
        for j in range(NCols):
            data[i][j] = max(m[i][j], self.data[i][j])
    return data
            
