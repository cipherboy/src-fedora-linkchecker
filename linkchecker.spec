%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_version: %define python_version %(%{__python} -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

Summary: Check HTML documents for broken links
Name: linkchecker
Version: 6.5
Release: 3%{?dist}
License: GPLv2
Group: Development/Tools
#Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source: http://downloads.sourceforge.net/linkchecker/LinkChecker-%{version}.tar.bz2
Source1: linkchecker.desktop
BuildRoot: %{_tmppath}/LinkChecker-%{version}-%{release}-root-%(%{__id_u} -n)
Url: http://linkchecker.sourceforge.net/
# qt4-devel is for qcollectiongenerator (HTML documentation)
BuildRequires: python-devel gettext qt4-devel

%description
Linkchecker is a simple script that checks HTML documents for broken links.

%prep
%setup -q -n LinkChecker-%{version}

%build
make -C doc/html/
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}
install -D -p --mode=644 doc/html/logo64x64.png %{buildroot}/usr/share/pixmaps/linkchecker.png
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

rm -f %{buildroot}%{python_sitearch}/LinkChecker-%{version}-py%{python_version}.egg-info

%find_lang LinkChecker

%clean
rm -rf %{buildroot}

%files -f LinkChecker.lang
%defattr(-,root,root,-)
%{_bindir}/linkchecker
%{python_sitearch}/linkcheck/
%{python_sitearch}/_LinkChecker_configdata.*
%{_mandir}/man1/linkchecker*.1*
%{_mandir}/man5/linkcheckerrc.5*
%lang(de) %{_mandir}/de/man1/linkchecker*.1*
%lang(de) %{_mandir}/de/man5/linkcheckerrc.5*
%{_datadir}/linkchecker
%doc readme.txt COPYING

%package gui
Summary: %{name}'s gui
Group: Development/Tools
Requires: linkchecker = %{version}-%{release} PyQt4 qscintilla-python
BuildRequires: desktop-file-utils

%description gui
A simple application that checks HTML documents for broken links.

%files gui
%{_bindir}/linkchecker-gui
%{_datadir}/applications/linkchecker.desktop
%{_datadir}/pixmaps/linkchecker.png

%changelog
* Wed May 11 2011 W. Michael Petullo <mike[at]flyn.org> - 6.5-3
- Bump release because last change did not propagate to F14/15

* Thu May 05 2011 W. Michael Petullo <mike[at]flyn.org> - 6.5-2
- Add qscintilla-python dependency to linkchecker-gui

* Mon Mar 21 2011 W. Michael Petullo <mike[at]flyn.org> - 6.5-1
- Update to upstream 6.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Apr 21 2010 W. Michael Petullo <mike[at]flyn.org> - 5.2-1
- Update to upstream 5.2
- Add .desktop file

* Sun Feb 14 2010 W. Michael Petullo <mike[at]flyn.org> - 5.1-1
- Update to upstream 5.1
- BuildRequire qt4-devel
- Build HTML documentation using make
- Handle new locations for installed files
- Add gui package

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 12 2008 W. Michael Petullo <mike[at]flyn.org> - 4.7-14
- Dynamically discover version (for .egg-info), do not hard code

* Sat Dec 12 2008 W. Michael Petullo <mike[at]flyn.org> - 4.7-13
- linkchecker-4.7-py2.5.egg-info -> 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.7-12
- Rebuild for Python 2.6

* Wed Feb 13 2008 W. Michael Petullo <mike[at]flyn.org> - 4.7-11
- Don't install linkchecker-4.7-py2.5.egg-info

* Mon Sep 10 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-10
- Bump version to retag with new sources

* Mon Sep 10 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-9
- Rebuild for F8

* Fri Jul 27 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-8
- On 64-bit platforms, everything is in %{python_sitearch}/linkcheck/

* Wed Jul 25 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-7
- Install configuration files in /etc/linkchecker
- Do not install examples

* Tue Jul 24 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-6
- Install logging.conf again
- Use %%find_lang

* Sat Jul 21 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-5
- Simplify %%files
- Don't install logging.conf because it is not documented
- Install linkcheckerrc into /etc/linkchecker

* Mon Jul 16 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-4
- Own %%{python_sitelib}/linkcheck/ and %%{python_sitearch}/linkcheck/
- Include .1.gz-style man pages in %%files
- Include _linkchecker_configdata.* instead of just .py

* Sat Jul 14 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-3
- Use sitearch for .so, sitelib for .py, .pyo and .pyc
- Clean up docs directory

* Thu Jul 12 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-2
- Use sitearch instead of sitelib
- Fix upstream source location
- Simplify %%files

* Wed Jul 11 2007 W. Michael Petullo <mike[at]flyn.org> - 4.7-1
- Rebuild for F7
- Update to upstream 4.7

* Thu Sep 07 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-11
- Rebuild for FC6

* Wed Sep 06 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-10
- Package /usr/lib/python2.4/site-packages/_linkchecker_configdata.py*

* Wed Sep 06 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-9
- Do not own %%{buildroot}%%{python_sitelib}

* Wed Sep 06 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-8
- Remove %%ghost from .pyo files: new Fedora policy

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-7
- Install /usr/lib/python2.4/site-packages/_linkchecker_configdata.pyc again

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-6
- Add %%{buildroot} to previous

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-5
- Do not install /usr/lib/python2.4/site-packages/_linkchecker_configdata.pyc

* Fri Jul 28 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-4
- Apply patch from Paul Howarth that fixes build on Rawhide (BZ 200282)

* Fri Feb 17 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-3
- Rebuild for Fedora Extras 5

* Mon Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-2
- Add some missing items to %%files

* Mon Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-1
- Update to linkchecker 3.3

* Sun Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
- Bump release number to re-import

* Sun Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
- ExcludeArch: x86_64.  I don't have one to test on

* Sun Oct 23 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-3
- %%dir appropriate directories

* Mon Sep 26 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-2
- Include LICENSE
- %%ghost .pyo files

* Sat Sep 17 2005 W. Michael Petullo <mike[at]flyn.org> - 3.2-1
- No longer use record option to setup.py
- Update to linkchecker 3.2

* Sun Nov 21 2004 W. Michael Petullo <mike[at]flyn.org> - 2.0-0.fdr.0.1.rc2
- Initial Fedora RPM release candidate, based on upstream SRPM
