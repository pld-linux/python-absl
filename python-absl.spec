# Python 3 version in python3-absl package
Summary:	Abseil Python Common Libraries
Summary(pl.UTF-8):	Wspólne biblioteki Abseil dla Pythona
Name:		python-absl
Version:	0.9.0
Release:	6
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/absl-py/
Source0:	https://files.pythonhosted.org/packages/source/a/absl-py/absl-py-%{version}.tar.gz
# Source0-md5:	4ba3484409252ec502b08f8ef8e48ab4
Patch0:		no-version.patch
URL:		https://github.com/abseil/abseil-py
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abseil Python is a collection of Python library code for building
Python applications. The code is collected from Google's own Python
code base, and has been extensively tested and used in production.

%description -l pl.UTF-8
Abseil Python to biblioteka Pythona będąca zbiorem kodu do tworzenia
aplikacji pythonowych. Kod bibliotek został zebrany z własnego kodu
Google'a w Pythonie, obszernie przetestowany i jest używany
produkcyjnie.

%prep
%setup -q -n absl-py-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/absl
%{py_sitescriptdir}/absl_py-%{version}-py*.egg-info
