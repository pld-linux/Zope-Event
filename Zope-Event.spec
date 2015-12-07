Summary:	Simple event system
Summary(pl.UTF-8):	Prosty system zdarzeń
Name:		Zope-Event
Version:	3.4.1
Release:	3
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz
# Source0-md5:	dedf8ec89b7852745accbee4aa5110e2
URL:		http://www.zope.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zope.event package provides a simple event system. It provides:
- an event publishing system
- a very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. (For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component)

%description -l pl.UTF-8
Pakiet zope.event udostępnia prosty system zdarzeń. Zawiera:
- system publikacji zdarzeń
- bardzo prosty system przekazywania zdarzeń, w oparciu o który można
  stworzyć bardziej wyszukane systemy przekazywania zdarzeń (na przykład
  system przekazywania zdarzeń oparty na typach, zbudowany w oparciu o
  zope.event, można znaleźć w zope.component)

%prep
%setup -q -n zope.event-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-purelib=%{py_sitedir} \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/event
%{py_sitedir}/zope.event-*.egg-info
%{py_sitedir}/zope.event-*-nspkg.pth
