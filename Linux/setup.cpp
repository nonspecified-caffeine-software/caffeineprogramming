#include <iostream>
#include <fstream>
#include <string>
#include <boost/algorithm/string/predicate.hpp>

using namespace std;
string fileName;
int i;
string content;

int main() {
	cout << "ENTER YOUR FILENAME";
	cin >> fileName;
	ifstream ncsFile;
	ofstream pyFile;
	if (boost::ends_with(fileName, ".ncs")) {
		ncsFile.open(fileName + ".ncs");
	}
	else {
		ncsFile.open(fileName);
	}
	pyFile.open("out.py");
    for(i=0 ; ncsFile.eof()!=true ; i++)
        content += ncsFile.get();
   ncsFile.close();
   pyFile << content;
	system("chmod +x NIXfatalError.bash");
	system("python3 out.py");
	return 0;
}
