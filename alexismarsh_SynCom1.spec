/*
A KBase module: alexismarsh_SynCom1
*/

module alexismarsh_SynCom1 {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_alexismarsh_SynCom1(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
