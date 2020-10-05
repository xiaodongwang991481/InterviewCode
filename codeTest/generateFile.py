import sys
import json

def generateCsvFile(csvIndex, records, metadataFile):
    csvFilename = 'part_%04d.csv' % csvIndex
    columns = set()
    for record in records:
        columns.addAll(record.keys())
    columns = list(columns)
    columns.sort()
    metadataFile.write("%s,\"%s\"\n" % (csvFilename, ",".join(columns)))
    csvFile = open(csvFilename, 'w')
    csvFile.write("%s\n" % ",".join(columns))
    for record in records:
        line = []
        for column in columns:
            value = record.get(column)
            if value is None:
                line.append('\\N')
            else:
                line.append(str(value))
        csvFile.write('%s' % ",".join(line))
    csvFile.close()

def generateFiles(metadataFilename):
    errorFile = open("erro_file", 'w')
    metadataFile = open(metadataFilename, 'w')
    metadataFile.write("filename,header\n")
    lines = 0
    records = []
    csvIndex = 0
    for line in sys.stdin:
        try:
            data = json.loads(line)
            if not isinstance(data, dict):
                raise Exception("%s is not a dict" % data)
            records.append(data)
            lines += 1
            if lines >= 100:
                generateCsvFile(csvIndex, records, metadataFile)
                lines = 0
                records = []
                csvIndex += 1
        except:
            errorFile.write(line)
    if lines > 0:
        generateCsvFile(csvIndex, records, metadataFile)
    metadataFile.close()
    errorFile.close()

if __name__ == "__main__":
    generateFiles("metadata_fileame")