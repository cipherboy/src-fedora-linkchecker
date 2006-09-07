%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Check HTML documents for broken links
Name: linkchecker
Version: 3.3
Release: 8%{?dist}
License: GPL
Group: Development/Tools
Source: http://dl.sf.net/linkchecker/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Url: http://linkchecker.sourceforge.net/
BuildRequires: python-devel
# Do not have one of these to test on:
ExcludeArch: x86_64

%description
Linkchecker is a simple script that checks HTML documents for broken links.

%prep
%setup -q

# Fix character encoding
iconv -f iso-8859-1 -t utf-8 -o linkchecker-de.1 doc/de/linkchecker.1
mv linkchecker-de.1 doc/de/linkchecker.1
iconv -f iso-8859-1 -t utf-8 -o linkchecker-fr.1 doc/fr/linkchecker.1
mv linkchecker-fr.1 doc/fr/linkchecker.1

# Avoid docfile dependency
sed -i -e 's:#!/usr/bin/env python.*:#!%{__python}:' doc/rest2htmlnav

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

# Collate list of python files
(
  echo '%defattr (0644,root,root,0755)'
  find %{buildroot}%{python_sitelib} -type d |
    sed 's:%{buildroot}\(.*\):%dir \1:'
  find %{buildroot}%{python_sitelib} -not -type d |
    sed 's:%{buildroot}\(.*\):\1:'
) > pyfiles

%clean
rm -rf %{buildroot}

%files -f pyfiles
%{_bindir}/linkchecker
%dir %{_datadir}/linkchecker/
%{_datadir}/linkchecker/*
%{_mandir}/man1/*
%doc TODO doc/ cgi/lconline/ test/ README LICENSE
%dir %{_mandir}/de/man1
%lang(de) %{_mandir}/de/man1/linkchecker.1*
%dir %{_mandir}/fr/man1
%lang(fr) %{_mandir}/fr/man1/linkchecker.1*

%changelog
* Wed Sep 06 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-8
   - Remove %%ghost from .pyo files: new Fedora policy.

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-7
   - Install /usr/lib/python2.4/site-packages/_linkchecker_configdata.pyc again.

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-6
   - Add %{buildroot} to previous.

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-5
   - Do not install /usr/lib/python2.4/site-packages/_linkchecker_configdata.pyc

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-4
   - Apply patch from Paul Howarth that fixes build on Rawhide (BZ
   200282).

* Fri Feb 17 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-3
   - Rebuild for Fedora Extras 5.

* Mon Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-2
   - Add some missing items to %%files.

* Mon Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-1
   - Update to linkchecker 3.3.

* Sun Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
   - Bump release number to re-import.

* Sun Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
   - ExcludeArch: x86_64.  I don't have one to test on.

* Sun Oct 23 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-3
   - %%dir appropriate directories.

* Mon Sep 26 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-2
   - Include LICENSE.
   - %%ghost .pyo files.

* Sat Sep 17 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-1
   - No longer use record option to setup.py.
   - Update to linkchecker 3.2.

* Sun Nov 21 2004 W. Michael Petullo <mike[at]flyn.org> - 2.0-0.fdr.0.1.rc2
   - Initial Fedora RPM release candidate, based on upstream SRPM.
