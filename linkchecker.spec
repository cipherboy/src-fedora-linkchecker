%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: Check HTML documents for broken links
Name: linkchecker
Version: 4.7
Release: 9%{?dist}
License: GPLv2
Group: Development/Tools
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1: linkchecker-4.7-fedora-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Url: http://linkchecker.sourceforge.net/
BuildRequires: python-devel gettext
# Do not have one of these to test on:
# ExcludeArch: x86_64

%description
Linkchecker is a simple script that checks HTML documents for broken links.

%prep
%setup -q
%patch1 -p1 -b .fedora-build

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

# The upstream installer does not seem to install these right:
%{__install} -D -m 0644 build/share/locale/de/LC_MESSAGES/linkchecker.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/linkchecker.mo
%{__install} -D -m 0644 build/share/locale/fr/LC_MESSAGES/linkchecker.mo %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/linkchecker.mo
%{__install} -D -m 0644 build/share/locale/es/LC_MESSAGES/linkchecker.mo %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/linkchecker.mo

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/linkchecker
#%ifarch x86_64 ppc64
%{python_sitearch}/linkcheck/
%{python_sitearch}/_linkchecker_configdata.*
#%else
#%{python_sitelib}/linkcheck/
#%{python_sitelib}/_linkchecker_configdata.*
#%endif
%config(noreplace) %{_sysconfdir}/linkchecker
%{_mandir}/man1/linkchecker.1*
%lang(de) %{_mandir}/de/man1/linkchecker.1*
%lang(fr) %{_mandir}/fr/man1/linkchecker.1*
%doc TODO doc/en README COPYING

%changelog
* Mon Sep 10 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-9
   - Rebuild for F7.

* Fri Jul 27 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-8
   - On 64-bit platforms, everything is in %{python_sitearch}/linkcheck/.

* Wed Jul 25 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-7
   - Install configuration files in /etc/linkchecker.
   - Do not install examples.

* Tue Jul 24 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-6
   - Install logging.conf again.
   - Use %%find_lang.

* Sat Jul 21 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-5
   - Simplify %%files.
   - Don't install logging.conf because it is not documented.
   - Install linkcheckerrc into /etc/linkchecker.

* Mon Jul 16 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-4
   - Own %%{python_sitelib}/linkcheck/ and %%{python_sitearch}/linkcheck/.
   - Include .1.gz-style man pages in %%files.
   - Include _linkchecker_configdata.* instead of just .py.

* Sat Jul 14 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-3
   - Use sitearch for .so, sitelib for .py, .pyo and .pyc.
   - Clean up docs directory.

* Thu Jul 12 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-2
   - Use sitearch instead of sitelib.
   - Fix upstream source location.
   - Simplify %%files.

* Wed Jul 11 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-1
   - Rebuild for F7.
   - Update to upstream 4.7.

* Thu Sep 07 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-11
   - Rebuild for FC6.

* Wed Sep 06 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-10
   - Package /usr/lib/python2.4/site-packages/_linkchecker_configdata.py*.

* Wed Sep 06 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-9
   - Do not own %%{buildroot}%%{python_sitelib}.

* Wed Sep 06 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-8
   - Remove %%ghost from .pyo files: new Fedora policy.

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-7
   - Install /usr/lib/python2.4/site-packages/_linkchecker_configdata.pyc again.

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-6
   - Add %%{buildroot} to previous.

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
