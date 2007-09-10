Summary:	zope.event package used in Zope 3
Name:		Zope-Event
Version:	3.4.0
Release:	0.1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://download.zope.org/distribution/zope.event-%{version}.tar.gz
# Source0-md5:	3a3d4bb9b6275149a05628262aba531f
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zope.event package used in Zope 3.

%prep
%setup -q -n zope.event-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/zope/event
%{py_sitescriptdir}/zope*egg*
%{py_sitescriptdir}/zope*pth
