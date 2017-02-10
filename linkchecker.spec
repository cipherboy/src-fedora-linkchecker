Name:           linkchecker
Version:        9.3
Release:        7%{?dist}
Summary:        Check HTML documents for broken links
License:        GPLv2
URL:            http://wummel.github.io/linkchecker/
Source0:        http://wummel.github.io/linkchecker/dist/LinkChecker-%{version}.tar.gz
# qt4-devel is for qcollectiongenerator (HTML documentation)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  qt4-devel
Requires:       python-requests

# Should be fixed upstream in next release; see:
# https://github.com/wummel/linkchecker/commit/c2ce810c3fb00b895a841a7be6b2e78c64e7b042
Patch0: fix-requests-version-bug.patch

%description
LinkChecker is a website validator. LinkChecker checks links in web documents or full websites.

Features:
- Recursive and multithreaded checking and site crawling
- Output in colored or normal text, HTML, SQL, CSV, XML or a sitemap graph in 
different formats
- HTTP/1.1, HTTPS, FTP, mailto:, news:, nntp:, Telnet and local file links 
support
- Restriction of link checking with regular expression filters for URLs
- Proxy support
- Username/password authorization for HTTP and FTP and Telnet
- Honors robots.txt exclusion protocol
- Cookie support
- HTML5 support
- HTML and CSS syntax check
- Antivirus check
- Different interfaces: command line, GUI and web interface
... and a lot more ...

%package        gui
Summary:        GUI program for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       PyQt4
Requires:       qscintilla-python

%description    gui
This package contains a GUI program for %{name}.

%prep
%setup -qn LinkChecker-%{version}

%patch0 -p1

%build
make -C doc/html/
CFLAGS="%{optflags}" %{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
install -pDm644 doc/html/logo64x64.png %{buildroot}%{_datadir}/pixmaps/linkchecker.png

# No need to import this package.
rm -frv %{buildroot}%{python2_sitearch}/LinkChecker-%{version}-py%{python2_version}.egg-info
# We don't need to let a terminal app have such file.
rm %{buildroot}%{_datadir}/applications/linkchecker.desktop

%find_lang linkchecker

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/linkchecker-gui.desktop

%files -f linkchecker.lang
%doc COPYING doc/changelog.txt doc/upgrading.txt
%{_bindir}/linkchecker
%{python2_sitearch}/linkcheck/
%{python2_sitearch}/linkcheck_dns/
%{python2_sitearch}/_LinkChecker_configdata.*
%{_mandir}/man1/linkchecker*.1*
%{_mandir}/man5/linkcheckerrc.5*
%lang(de) %{_mandir}/de/man1/linkchecker*.1*
%lang(de) %{_mandir}/de/man5/linkcheckerrc.5*
%{_datadir}/linkchecker/

%files gui
%{_bindir}/linkchecker-gui
%{_datadir}/applications/linkchecker-gui.desktop
%{_datadir}/pixmaps/linkchecker.png

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Charalampos Stratakis <cstratak@redhat.com> - 9.3-6
- Backport upstream patch to fix python-requests version error

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 05 2014 Christopher Meng <rpm@cicku.me> - 9.3-1
- Update to 9.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Christopher Meng <rpm@cicku.me> - 9.2-1
- Update to 9.2

* Tue Apr 01 2014 Christopher Meng <rpm@cicku.me> - 9.1-1
- Update to 9.1

* Sat Mar 08 2014 Christopher Meng <rpm@cicku.me> - 9.0-1
- Update to 9.0

* Fri Jan 10 2014 Christopher Meng <rpm@cicku.me> - 8.6-2
- Add some missing docs.

* Thu Jan 09 2014 Christopher Meng <rpm@cicku.me> - 8.6-1
- Major update to 8.6
- SPEC cleanup.
- Standardize desktop files.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

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

* Fri Dec 12 2008 W. Michael Petullo <mike[at]flyn.org> - 4.7-14
- Dynamically discover version (for .egg-info), do not hard code

* Fri Dec 12 2008 W. Michael Petullo <mike[at]flyn.org> - 4.7-13
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

* Tue Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-2
- Add some missing items to %%files

* Tue Jan 03 2006 W. Michael Petullo <mike[at]flyn.org> - 3.3-1
- Update to linkchecker 3.3

* Mon Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
- Bump release number to re-import

* Mon Jan 02 2006 W. Michael Petullo <mike[at]flyn.org> - 3.2-4
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
