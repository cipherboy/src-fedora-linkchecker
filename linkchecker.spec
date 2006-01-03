%define pythonver 2.4
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Check HTML documents for broken links
Name: linkchecker
Version: 3.3
Release: 2
License: GPL
Group: Development/Tools
Source: http://dl.sf.net/linkchecker/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Url: http://linkchecker.sourceforge.net/
BuildRequires: python-devel
Requires: python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")
# Do not have one of these to test on:
ExcludeArch: x86_64

%description
Linkchecker is a simple script that checks HTML documents for broken links.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT
# %find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

# %files -f %{name}.lang
%files
%defattr(-,root,root)
%{_bindir}/linkchecker
%{python_sitelib}/*.py
%dir %{python_sitelib}/linkcheck/
%{python_sitelib}/linkcheck/*.py
%{python_sitelib}/linkcheck/*.pyc
%ghost %{python_sitelib}/linkcheck/*.pyo
%dir %{python_sitelib}/linkcheck/HtmlParser/
%{python_sitelib}/linkcheck/HtmlParser/*.py
%{python_sitelib}/linkcheck/HtmlParser/*.pyc
%{python_sitelib}/linkcheck/HtmlParser/*.so
%ghost %{python_sitelib}/linkcheck/HtmlParser/*.pyo
%dir %{python_sitelib}/linkcheck/ftpparse/
%{python_sitelib}/linkcheck/ftpparse/*.py
%{python_sitelib}/linkcheck/ftpparse/*.pyc
%{python_sitelib}/linkcheck/ftpparse/*.so
%ghost %{python_sitelib}/linkcheck/ftpparse/*.pyo
%dir %{python_sitelib}/linkcheck/checker/
%{python_sitelib}/linkcheck/checker/*.py
%{python_sitelib}/linkcheck/checker/*.pyc
%ghost %{python_sitelib}/linkcheck/checker/*.pyo
%dir %{python_sitelib}/linkcheck/dns/
%{python_sitelib}/linkcheck/dns/*.py
%{python_sitelib}/linkcheck/dns/*.pyc
%ghost %{python_sitelib}/linkcheck/dns/*.pyo
%dir %{python_sitelib}/linkcheck/logger/
%{python_sitelib}/linkcheck/logger/*.py
%{python_sitelib}/linkcheck/logger/*.pyc
%ghost %{python_sitelib}/linkcheck/logger/*.pyo
%dir %{python_sitelib}/linkcheck/dns/rdtypes/ANY
%{python_sitelib}/linkcheck/dns/rdtypes/ANY/*.py
%{python_sitelib}/linkcheck/dns/rdtypes/ANY/*.pyc
%ghost %{python_sitelib}/linkcheck/dns/rdtypes/ANY/*.pyo
%dir %{python_sitelib}/linkcheck/dns/rdtypes/IN
%{python_sitelib}/linkcheck/dns/rdtypes/IN/*.py
%{python_sitelib}/linkcheck/dns/rdtypes/IN/*.pyc
%ghost %{python_sitelib}/linkcheck/dns/rdtypes/IN/*.pyo
%dir %{python_sitelib}/linkcheck/dns/rdtypes
%{python_sitelib}/linkcheck/dns/rdtypes/*.py
%{python_sitelib}/linkcheck/dns/rdtypes/*.pyc
%ghost %{python_sitelib}/linkcheck/dns/rdtypes/*.pyo
%dir %{_datadir}/linkchecker/
%{_datadir}/linkchecker/*
%{_mandir}/man1/*
%doc TODO doc/ cgi/lconline/ test/ README LICENSE

%changelog
* Mon Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-2
   - Add some missing items to %%files.

* Mon Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-1
   - Update to linkchecker 3.3.

* Sun Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
   - Bump release number to re-import.

* Sun Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
   - ExcludeArch: x86_64.  I don't have one to test on.

* Sun Oct 23 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-3
   - %dir appropriate directories.

* Mon Sep 26 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-2
   - Include LICENSE.
   - %ghost .pyo files.

* Sat Sep 17 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-1
   - No longer use record option to setup.py.
   - Update to linkchecker 3.2.

* Sun Nov 21 2004 W. Michael Petullo <mike[at]flyn.org> - 2.0-0.fdr.0.1.rc2
   - Initial Fedora RPM release candidate, based on upstream SRPM.
