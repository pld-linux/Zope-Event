Summary:	Simple event system
Name:		Zope-Event
Version:	3.4.0
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://download.zope.org/distribution/zope.event-%{version}.tar.gz
# Source0-md5:	3a3d4bb9b6275149a05628262aba531f
URL:		http://www.zope.org/
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zope.event package provides a simple event system.  It provides:
- an event publishing system
- a very simple event-dispatching system on which more sophisticated event
  dispatching systems can be built.  (For example, a type-based event
  dispatching system that builds on zope.event can be found in
  zope.component


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
