import pip_audit.format as format


def test_columns(vuln_data):
    columns_format = format.ColumnsFormat()
    expected_columns = """Package Version ID     Description              Affected Versions
------- ------- ------ ------------------------ -----------------
foo     1.0     VULN-0 The first vulnerability  1.1,1.4
foo     1.0     VULN-1 The second vulnerability 1.0
bar     0.1     VULN-2 The third vulnerability"""
    assert columns_format.format(vuln_data) == expected_columns