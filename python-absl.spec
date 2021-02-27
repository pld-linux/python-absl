#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Abseil Python Common Libraries
Summary(pl.UTF-8):	Wspólne biblioteki Abseil dla Pythona
Name:		python-absl
Version:	0.9.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/absl-py/
Source0:	https://files.pythonhosted.org/packages/source/a/absl-py/absl-py-%{version}.tar.gz
# Source0-md5:	4ba3484409252ec502b08f8ef8e48ab4
URL:		https://github.com/abseil/abseil-py
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
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

%package -n python3-absl
Summary:	Abseil Python Common Libraries
Summary(pl.UTF-8):	Wspólne biblioteki Abseil dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-absl
Abseil Python is a collection of Python library code for building
Python applications. The code is collected from Google's own Python
code base, and has been extensively tested and used in production.

%description -n python3-absl -l pl.UTF-8
Abseil Python to biblioteka Pythona będąca zbiorem kodu do tworzenia
aplikacji pythonowych. Kod bibliotek został zebrany z własnego kodu
Google'a w Pythonie, obszernie przetestowany i jest używany
produkcyjnie.

%prep
%setup -q -n absl-py-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/absl
%{py_sitescriptdir}/absl_py-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-absl
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/absl
%{py3_sitescriptdir}/absl_py-%{version}-py*.egg-info
%endif
